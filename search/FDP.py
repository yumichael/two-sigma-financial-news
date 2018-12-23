from common import *
from search.imports import *
from search.file import *

lgbNullDataset = lgb.Dataset(pd.DataFrame({'_a_': np.arange(88), '_b_': np.arange(88)}))

class FDP(O()):
    '''data transformation code inside `op` object:

    client --save(+write)--> disk; client --keep--> memory; disk --load(+read)--> memory

    read = text/bytes stream -> as-is object read from file
    write = object to save as is to file -> text/bytes stream
    load = as-is object read from file -> object to be loaded in memory
    save = raw object given by client -> object to save as-is to file
    keep = as-is object read from file -> object to keep in memory
    keepClient = raw object given by client -> object to keep in memory
    '''

    key = 'Params'
    keyFunc = lambda params: tuple(sorted(dict.items(params)))

    class op(O()):
        @IDSSH.json
        class Params(O()):
            '''just a dict of the parameter value assignments'''
            keepClient = dict
            
        @IDSSH.json
        class Results(O()):
            '''should be a dict-like of various things, most importantly including "score"'''
            load = lambda x: O(**x)
            save = pydict
            keepClient = lambda x: O.mycopy(x) if isinstance(x, O) else O(**x)
            
        @IDSSH.pickle
        class Training(O()):
            '''tuple (aligning with samples training/cv split tuple) of LightGBM training eval DataFrames'''
            keep = False
            
        @IDSSH.pickle
        class Boosters(O()):
            '''the actual lgb.Booster model. well, a tuple of them, one for each cv set'''
            #read = lambda file: lgb.Booster(model_file=file)
            load = lambda x: tuple(lgb.Booster(train_set=lgbNullDataset).model_from_string(s, verbose=False) for s in x)
            #write = lambda x, file: x.save_model(file)
            save = lambda x: tuple(b.model_to_string() for b in x)
            keep = False

        @IDSSH.json
        class Tags(O()):
            '''just a list of #hashtags lol jk'''
            load = False #frzset
            save = False #sorted
            keep = False #load
            
        @IDSSH.pickle
        class Answers(O()):
            '''a list (per kfold) of list ([0] is cv, rest are holdout) of the dataframes of the actual prediction results'''