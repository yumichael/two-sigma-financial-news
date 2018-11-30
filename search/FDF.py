from common import *
from search.imports import *
from search.file import *

class FDF(O()):
    key = 'Feats'
    keyFunc = lambda features: features # internally already coverted to immutable
    keyFuncClient = frzset
    class op(O()):
        '''container of feature name strings'''
        @IDSSH.json
        class Feats(O()):
            load = frozenset
            save = sorted
            keepClient = frozenset
        @IDSSH.json
        class Ctor(O()):
            '''should be just a string, the query string of the FFF object'''