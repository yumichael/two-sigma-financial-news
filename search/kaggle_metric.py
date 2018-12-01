class KaggleMetric():
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
        std = x_t_sum.std()
        score = x_t_sum.mean() / std if std != 0 else x_t_sum.mean()

        valid_data.i += self.incr
        return 'kaggle', score+valid_data.i, True