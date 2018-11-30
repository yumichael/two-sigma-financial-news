from common import *
from search.imports import *
from search.file import *

class FDS(O()):
    key = 'Ctor'
    keyFunc = lambda ctor: ctor #samples: samples # internally already converted immutable
    keyFuncClient = lambda ctor: frzset(frzset(s) for s in ctor) #samples:frzset((frzset(tr),frzset(cv))for tr,cv in samples)
    class op(O()):
        @IDSSH.json
        class Samps(O()):
            '''tuple (num samples) of 2-tuples of tr/cv containers of the canonical index values for the split'''
            load = lambda samples: frzset((frzset(tr), frzset(cv)) for tr, cv in samples)
            save = False # too big to save #lambda samples: sorted([sorted(tr), sorted(cv)] for tr, cv in samples)
            keepClient = load
        @IDSSH.json
        class Ctor(O()):
            '''should be container = {tr, cv}, where tr and cv are containers of the "quarter" value in the resp. data set'''
            #'''should be O specs object'''
            load = lambda ctor: frzset(frzset(s) for s in ctor)
            save = lambda ctor: sorted(sorted(s) for s in ctor)
            keepClient = compose(save, load)