import numpy as np
from numba import njit


@njit
def make_blocks(values):
    '''Return [] of (start,end(excl)) indices of blocks of same values in `values`'''
    ans = []
    i = 0
    prev_x = values[0]
    for i,x in enumerate(values):
        if i==0:
            start = i
            prev_x = x
        elif prev_x!=x:
            ans.append((start,i))
            start = i
            prev_x = x
    ans.append((start,len(values)))
    return ans

@njit
def blocks_sum(blocks, values):
    return np.array([values[i:j].sum() for i,j in blocks])

@njit
def tanh_trans(a, shrink):
    '''transform `a` by tanh centered at `a.mean()` with shrink factor `shrink`'''
    center = a.mean()
    return np.tanh((a-center) * shrink) + center

@njit
def kaggle_score(blocks, x, y):
    xy = x * y
    t = np.array([xy[i:j].sum() for i,j in blocks])
    std = t.std()
    return t.mean()/std if std!=0 else 0.

@njit
def kaggle_tt_score(blocks, x, y, shrink):
    t = np.array([(tanh_trans(x[i:j], shrink) * y[i:j]).sum() for i,j in blocks])
    std = t.std()
    return t.mean()/std if std!=0 else 0.


class KaggleMetric():
    score = 'sharpe'
    
    #def __init__(self, incr=0):
    #    self.incr = incr
    
    def attach(self, ms):
        L, s = ms._L, ms._s
        for Ltr, Lcv, tr, cv in zip(L.tr, L.cv, s.tr, s.cv):
            Ltr.timeFactor = ms.Y.time[tr].factorize()[0]
            Lcv.timeFactor = ms.Y.time[cv].factorize()[0]
            Ltr.value = (ms.Y.upDown*(ms.Y[ms.specs.model.weight] if 'weight' in ms.specs.model else 1.))[tr]
            Lcv.value = (ms.Y.upDown*(ms.Y[ms.specs.model.weight] if 'weight' in ms.specs.model else 1.))[cv]
            #Ltr.i = 0
            #Lcv.i = 0
            Ltr.blocks = make_blocks(Ltr.timeFactor)
            Lcv.blocks = make_blocks(Lcv.timeFactor)
        for Lho, ho in zip(ms.Lho, ms.ho): #NEW for k-fold flow
            Lho.timeFactor = ms.Y.time[ho].factorize()[0]
            Lho.value = (ms.Y.upDown*(ms.Y[ms.specs.model.weight] if 'weight' in ms.specs.model else 1.))[ho]
            #Lho.i = 0
            Lho.blocks = make_blocks(Lho.timeFactor)
    
    def __call__(self, preds, valid_data):
        values = valid_data.value
        blocks = valid_data.blocks
        
        preds = preds*2-1
        x, y = preds, values.values
        
        #trans = [] #[3, 7, 12, 18, 25] # new flow with multiple transformations
        
        #def iter_trans_scores(trans):
        #    yield kaggle_score(blocks, x, y)
        #    for shrink in trans:
        #        yield kaggle_tt_score(blocks, x, y, shrink)
        
        #return list(zip(['sharpe']+[f'sharpe_tt{t}' for t in trans], iter_trans_scores(trans), [True]*(1+len(trans))))
        
        t = blocks_sum(blocks, x*y)
        var = t.var(ddof=0) # std to var is #NEW
        mean = t.mean() #NEW
        score = mean / np.sqrt(var) if var != 0 else mean

        #valid_data.i += self.incr #NEW comment out
        return [('sharpe', score, True), ('mean', mean, True), ('var', var, False)] #NEW
    
        #return 'kaggle', score+valid_data.i, True
    
#     @staticmethod #NEW that it's deleted for k-fold flow
#     def func(bst, F, P, weight):
#         guess = bst.predict(F)*2-1
#         guess = guess*(np.abs(guess)>=0.0)
#         P['trade'] = guess*P.upDown*P[weight]
#         daily = P.groupby('time').trade.sum()
#         del P['trade']
#         return [('mean', daily.mean()/daily.std(ddof=0)