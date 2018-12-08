import numpy as np

class KaggleMetric():
    score = 'sharpe'
    
    def __init__(self, incr=0):
        self.incr = incr
    
    def attach(self, ms):
        L, s = ms._L, ms._s
        for Ltr, Lcv, tr, cv in zip(L.tr, L.cv, s.tr, s.cv):
            Ltr.timeFactor = ms.Y.time[tr].factorize()[0]
            Lcv.timeFactor = ms.Y.time[cv].factorize()[0]
            Ltr.value = (ms.Y.upDown*(ms.Y[ms.specs.model.weight] if 'weight' in ms.specs.model else 1.))[tr]
            Lcv.value = (ms.Y.upDown*(ms.Y[ms.specs.model.weight] if 'weight' in ms.specs.model else 1.))[cv]
            Ltr.i = 0
            Lcv.i = 0
        for Lho, ho in zip(ms.Lho, ms.ho): #NEW for k-fold flow
            Lho.timeFactor = ms.Y.time[ho].factorize()[0]
            Lho.value = (ms.Y.upDown*(ms.Y[ms.specs.model.weight] if 'weight' in ms.specs.model else 1.))[ho]
            Lho.i = 0
    
    def __call__(self, preds, valid_data):
        df_time = valid_data.timeFactor
        #labels = valid_data.get_label()
        values = valid_data.value
        #assert len(labels) == len(df_time)

        preds = preds*2-1
        #labels = labels*2-1
        x_t = preds * values

        # Here we take advantage of the fact that `labels` (used to calculate `x_t`)
        # is a pd.Series and call `group_by`
        x_t_sum = x_t.groupby(df_time).sum()
        var = x_t_sum.var() # std to var is #NEW
        mean = x_t_sum.mean() #NEW
        score = mean / np.sqrt(var) if var != 0 else mean

        valid_data.i += self.incr #NEW comment out
        return [('sharpe', score+valid_data.i, True), ('mean', mean, True), ('var', var, False)] #NEW
        #return 'kaggle', score+valid_data.i, True
    
#     @staticmethod #NEW that it's deleted for k-fold flow
#     def func(bst, F, P, weight):
#         guess = bst.predict(F)*2-1
#         guess = guess*(np.abs(guess)>=0.0)
#         P['trade'] = guess*P.upDown*P[weight]
#         daily = P.groupby('time').trade.sum()
#         del P['trade']
#         return [('mean', daily.mean()/daily.std(ddof=0)