from common import *
from search.imports import *

class LSP(O()):
    class Discrete(O()):
        stop = {1:.45, 2:.5, 3:.55, 5:.6, 7:.65, 9:.7} #{1:.3, 3:.5, 5:.6, 7:.65}
        obo = {0: 0}
        enc = {
            'learning_rate': [.05],
            ('max_depth','num_leaves'):
                [(6,1<<6),(8,1<<8),(10,1<<10),(12,1<<12),
                 (10,1<<6),(-1,1<<10),(10,1<<8),(-1,1<<14),
                 (12,1<<10),(8,1<<6),(-1,1<<12),(12,1<<8),]
        }
        
    class OneByOne(O()):
        base = .33
        class info(O()):
            a = "main [a]rray data of 3 values, [min mid max]"
            b =  "[b]ack up value, i.e. default value if array doesn't give better results"
            cast = "function to apply to values before using to cast to the right dtype"
            lim = "maximum number of iterations of searching in this hyperparameter"
        class default(O()):
            cast = keepSigFig(2)
            lim = 0
        enc = {#TODO implement 1 sided search e.g. len(a)==2
            0: {
                'min_data_in_leaf': O(a=[1,60,375], b=120, cast=round, lim=lambda lim: lim),
                'min_sum_hessian_in_leaf': O(a=[0,50,200], lim=lambda lim: lim+1),
                'lambda_l1': O(a=[0,.02,.2], b=0),
                'lambda_l2': O(a=[0,.02,.2], b=0),
            }
        }