from common import *

class TP(O()):
    _ = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|doo|dcc|doc|daoc|vp1dd)
            & index[0,1,2, 0:1,1:2,0:2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|doo|vp1dd|vp5dd|Volatility)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|doo|vp1dd|vp5dd|Volatility)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|doo[1:]|oo{.&[10:]}|aoo[10:]|doo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Max&index[0,5,10,20]}
                | Drawup[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0,5,10,20]}
              )
            & Since[21:,62:,125:,250:]
          )
        | (
            <>Return{dd} & VP[1:, 5:, 10:]
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Max & index[0,5,10,20]}
                | Drawup[1, 5:,10:,20:, 10:5,20:10]
                | Since{Min & index[0,5,10,20]}
              )
            & Since[21:,62:,125:,250:]
          )
        | (
            <> Volatility[20:,60:]
            | Volatility[10:,20:]
            & (
                <>Drawdown[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Max & index[0,5,10,20]}
                | Drawup[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Min & index[0,5,10,20]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    | Market{.&
        <>(~Weight|Weight)
        & (Return|VP|Volatility)
        & [1:,5:,10:,20:,60:]
      }
    |
        <>Return{pure&~dd} & VP[1:,5:,10:,20:,60:]
        | FracRec[21:,62:,125:,250:]
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume | Open | Close}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    |
        Time{long|short}
    '''
    ################################################# the s<number> guys #########################################
    s00 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(oo|cc|aoo|acc|doo|vp1dd)\n            & index[0,1,2, 0:1,0:2]\n          }\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|aoo|vp1dd)\n            & [5:,10:,15:,15:10,20:15,15:5,20:10]\n          }\n        | (\n            <>Return{(oo{.&[1:]})}\n            & (\n                | Drawdown[10:,20:]\n                | Since{Max&index[10,20]}\n                | Drawup[1:]\n                | Since{Min&index[0,5]}\n              )\n            & Since[ 62:, 250:]\n          )\n        | (\n            <> Volatility[ 60:]\n            | Volatility[ 20:]\n            & (\n                | Since{Max & index[0,5]}\n                | Drawup[ 10:5,20:10]\n                | Since{Min & index[20]}\n              )\n            & Since[ 62:, 250:]\n          )\n      )\n    |\n        <>Return{pure&~dd} & VP[10:]\n    |'
    s01 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(oo|cc|vp1dd)\n            & index[1,2, 0:1,1:2,0:2]\n          }\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|aoo|vp1dd)\n            & [10:,15:,10:5,20:15,15:5,20:10]\n          }\n        | (\n            <>Return{(oo{.&[1:]}|oo{.&[10:]})}\n            & (\n                | Drawdown[10:,20:, 10:5]\n                | Since{Min&index[0]}\n              )\n            & Since[21:, 125:, 250:]\n          )\n      )\n    |\n        <>AssetEnc{InUni}\n        | AssetEnc{Code}'
    s02 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(daoc|vp1dd)\n            & index[0,1:2,0:2]\n          }\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|aoo|vp1dd)\n            & [6:,9:,12:,15:,12:9,18:12,15:6,15:3,18:6,21:9]\n          }\n        | (\n            <>Return{(oo{.&[10:]})}\n            & (\n                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}\n                | Drawdown[1:, 5:,20:,20:10]\n                | Since{Min&index[20]}\n              )\n            & Since[21:, 62:, 125:, 250:]\n          )\n      )\n    |\n        | FracRec[21:,62:,125:,250:]\n    |\n        Time{long| short}'
    s03 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(oo|cc|vp1dd)\n            & index[1,2, 0:1,1:2,0:2]\n          }\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|aoo|vp1dd)\n            & [10:,15:,10:5,20:15,15:5,20:10]\n          }\n        | (\n            <>Return{(oo{.&[1:]}|oo{.&[10:]})}\n            & (\n                | Drawdown[10:,20:, 10:5]\n                | Since{Min&index[0]}\n              )\n            & Since[21:, 125:, 250:]\n          )\n      )\n    |\n        <>AssetEnc{InUni}\n        | AssetEnc{Code}'
    s10 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(oo|cc|dcc)\n            & index[0,1,2, 0:1,1:2]\n          }\n        | (\n            <>Return{(oo{.&[1:]}|oo{.&[10:]}|doo[10:])}\n            & (\n                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}\n                | Drawdown[1:, 5:,10:, 10:5]\n                | Since{Max&index[0]}\n                | Since{Min&index[0,5]}\n              )\n            & Since[21:, 125:, 250:]\n          )\n        | (\n            <>Return{dd} & VP[1:, 5:, 10:]\n            & (\n                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}\n                | Since{Max & index[5]}\n                | Drawup[20:10]\n                | Since{Min & index[20]}\n              )\n            & Since[21:, 125:, 250:]\n          )\n        | (\n            <> Volatility[ 60:]\n            | Volatility[10:]\n            & (\n                | Since{Max & index[20]}\n                | Since{Min & index[20]}\n              )\n            & Since[21:, 125:, 250:]\n          )\n      )\n    |\n        Time{long| short}'
    s11 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(oo|cc|acc|doo|dcc|daoc)\n            & index[0,1]\n          }\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(aoo|doo|vp1dd|vp5dd|Volatility)\n            & [10:,10:5,15:5,20:5]\n          }\n        | (\n            <>Return{(oo{.&[1:]}|oo{.&[10:]})}\n            & (\n                | Drawdown[1:,10:, 10:5,20:10]\n                | Since{Max&index[10]}\n                | Drawup[20:10]\n                | Since{Min&index[0]}\n              )\n            & Since[21:, 62:, 125:, 250:]\n          )\n        | (\n            <>Return{dd} & VP[1:, 10:]\n            & (\n                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}\n                | Since{Max & index[0]}\n                | Since{Min & index[0]}\n              )\n            & Since[21:, 62:, 125:, 250:]\n          )\n      )\n    |\n        <>FaceValue{ Close}\n        | Return{mix[1,3,5,6,7,8,9,11,12,13,14,18,19]}\n        | Return{rr}'
    s20 = '    <>~Market & (\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|aoo|vp1dd|Volatility)\n            & [15:,6:3,9:6,12:9,12:6,18:12,18:9,21:12,18:6,21:9,18:3,21:6,21:3]\n          }\n        | (\n            <>Return{(oo{.&[10:]}|doo[10:])}\n            & (\n                | Drawdown[ 5:,10:,20:]\n                | Since{Max&index[0,5]}\n                | Since{Min&index[0,5]}\n              )\n            & Since[21:, 62:, 250:]\n          )\n        | (\n            <> Volatility[ 60:]\n            | Volatility[10:, 20:]\n            & (\n                | Since{Max & index[0,5]}\n                | Since{Min & index[10]}\n              )\n            & Since[ 250:]\n          )\n      )\n    |\n        <>Return{pure&~dd} & VP[60:]\n        | FracRec[21:]\n    |\n        Time{long}'
    s21 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(vp1dd)\n            & index[0,2, 0:1]\n          }\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(doo|vp5dd|Volatility)\n            & [5:,15:,10:5,15:10,20:15,15:5,20:5]\n          }\n        | (\n            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]})}\n            & (\n                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}\n                | Drawdown[1:,10:,20:]\n                | Since{Max&index[0,10]}\n                | Since{Min&index[0,20]}\n              )\n            & Since[21:, 125:, 250:]\n          )\n      )\n    | Market{.&\n        <>(~Weight)\n        & (Return| Volatility)\n        & [20:,60:]\n      }\n    |\n        | FracRec[21:,125:,250:]\n    |'
    s22 = '    <>~Market & (\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|aoo|doo|vp1dd|vp5dd)\n            & [10:,10:5,15:10,15:5,20:5]\n          }\n        | (\n            <>Return{(oo{.&[1:]})}\n            & (\n                | Drawdown[10:,20:10]\n                | Since{Max&index[20]}\n                | Since{Min&index[20]}\n              )\n            & Since[21:, 250:]\n          )\n        | (\n            <>Return{dd} & VP[ 5:, 10:]\n            & (\n                | Drawdown[1:]\n                | Since{Max & index[0]}\n                | Since{Min & index[0]}\n              )\n            & Since[21:, 250:]\n          )\n      )\n    |\n        Time{long| short}'
    s23 = '    <>~Market & (\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|aoo|doo|vp1dd|vp5dd)\n            & [10:,10:5,15:10,15:5,20:5]\n          }\n        | (\n            <>Return{(oo{.&[1:]})}\n            & (\n                | Drawdown[10:,20:10]\n                | Since{Max&index[20]}\n                | Since{Min&index[20]}\n              )\n            & Since[21:, 250:]\n          )\n        | (\n            <>Return{dd} & VP[ 5:, 10:]\n            & (\n                | Drawdown[1:]\n                | Since{Max & index[0]}\n                | Since{Min & index[0]}\n              )\n            & Since[21:, 250:]\n          )\n      )\n    |\n        Time{long| short}'
    s24 = '    <>~Market & (\n        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&\n            <>(oo|daoc)\n            & index[0,1,2, 0:1,0:2]\n          }\n        | Return{.&pure&~index} & ~Since & Return{.&\n            <>(oo|doo)\n            & [10:,15:,20:15,15:5,20:10,20:5]\n          }\n        | (\n            <>Return{(oo{.&[1:]}|oo{.&[10:]}|doo[10:])}\n            & (\n                | Drawdown[ 5:,20:10]\n                | Since{Min&index[0]}\n              )\n            & Since[21:]\n          )\n        | (\n            <>Return{dd} & VP[1:, 5:]\n            & (\n                | Since{Max & index[0,10]}\n                | Since{Min & index[0]}\n              )\n            & Since[21:]\n          )\n      )\n    |\n        <>AssetEnc{InUni}'

    ################################################ END s<number> guys #############################################################
    
    IKGCover = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverTenDraw = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverThree = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverThreeVP1 = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc|vp1dd)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|vp1dd)}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverThreeNoShort = '''
    <>~Market & (
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverThreeMoreShort = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0,1,2,0:1,1:2,0:2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverThreeHomo = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverThreeNoDraw = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
      )
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverVolatility = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Since{Max & index[0,10]}
                | Since{Min & index[0,10]}
              )
            & Since[21:,65:,125:,250:]
          )
      )
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    IKGCoverHomo = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
    '''
    
    TryIt = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,125:,250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Drawdown[20:]
                | Since{Max & index[0,20]}
                | Drawup[1:, 20:10]
              )
            & Since[21:,125:,250:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,125:,250:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    TryItVP5 = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp5dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,125:,250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Drawdown[20:]
                | Since{Max & index[0,20]}
                | Drawup[1:, 20:10]
              )
            & Since[21:,125:,250:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,125:,250:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    TryItHalfYear = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,62:,125:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Drawdown[20:]
                | Since{Max & index[0,20]}
                | Drawup[1:, 20:10]
              )
            & Since[21:,62:,125:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,62:,125:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    TryMoreStandard = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,62:,125:,250:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    ############################## fuck forgot that ikg actually kills the non-homo features #######################
    
    IKGZen = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{RandMap[0,1]}
    '''
    
    IKGZenTenDraw = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{RandMap[1,0]}
    '''
    
    IKGHomoTenDraw = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    '''
    
    IKGZenThree = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{RandMap[2,3]}
    '''
    
    IKGZenThreeVP1 = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc|vp1dd)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|vp1dd)}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{RandMap[2,3]}
    '''
    
    IKGZenThreeMoreShort = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0,1,2,0:1,1:2,0:2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>AssetEnc{RandMap[2,3]}
    '''
    
    IKGHomoThree = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    '''
    
    IKGZenVolatility = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Since{Max & index[0,10]}
                | Since{Min & index[0,10]}
              )
            & Since[21:,65:,125:,250:]
          )
      )
    |
        <>AssetEnc{RandMap[4,5]}
    '''
    
    IKGHomoVolatility = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Since{Max & index[0,10]}
                | Since{Min & index[0,10]}
              )
            & Since[21:,65:,125:,250:]
          )
      )
    |
    '''
    
    IKGHomo = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    '''
    
    Another = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2,0:1,1:2,0:2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|vp1dd)}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:5,20:10]
                | Since{Min&index[0,10]}
                | Drawup[5:,10:5,20:10]
                | Since{Max&index[0,10]}
              )
            & Since[21:,62:]
          )
      )
    |
        Time{long | short}
    '''
    
    Global = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|doo|dcc|doc|daoc)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|doo)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|doo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:,10:,20:,]
                | Since{Max&index[0,20]}
                | Since{Min&index[0,20]}
              )
            & Since[21:,62:,250:]
          )
        | (
            <> Volatility[20:,60:]
          )
      )
    | Market{.&
        <>(Weight)
        & (VP|Volatility)
        & [20:,60:]
      }
    |
        <>Return{pure&~dd} & VP[20:,60:]
        | FracRec[250:]
    '''
    
    TryIt = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,125:,250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Drawdown[20:]
                | Since{Max & index[0,20]}
                | Drawup[1:, 20:10]
              )
            & Since[21:,125:,250:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,125:,250:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    TryItVP5 = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp5dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,125:,250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Drawdown[20:]
                | Since{Max & index[0,20]}
                | Drawup[1:, 20:10]
              )
            & Since[21:,125:,250:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,125:,250:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    TryItHalfYear = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,62:,125:]
          )
        | (
            <> Volatility[60:]
            | Volatility[20:]
            & (
                | Drawdown[20:]
                | Since{Max & index[0,20]}
                | Drawup[1:, 20:10]
              )
            & Since[21:,62:,125:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,62:,125:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    TryMoreStandard = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]}|aoo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
    |
        <>Return{pure&~dd} & VP[10:,20:]
        | FracRec[21:,62:,125:,250:]
    |
        <>AssetEnc{InUni}
    |
        Time{long | short}
    '''
    
    ############################################# uh other stuff below like pairs #################################################
    
    
    SearchedPair = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|doo|doc)
            & index[0,1,2, 0:1,1:2,0:2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|doo|vp5dd|Volatility)
            & [5:,15:,10:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                | Drawdown[1:]
                | Since{Max&index[0]}
                | Drawup[1:,10:]
                | Since{Min&index[0,10]}
              )
            & Since[21:, 62:, 125:, 250:]
          )
        | (
            <> Volatility[20:]
            | Volatility[ 20:]
            & (
                <>Drawdown[20:10]
                | Since{Max & index[10]}
                | Since{Min & index[5,10]}
              )
            & Since[21:, 62:, 125:, 250:]
          )
      )
#<>#
    <>~Market & (
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp5dd)
            & [5:,20:10,20:5]
          }
      )
#<>#
0
#<>#
    <>0
    | Corr & Corr{
        <>[21,250]
        & aoo
      }
    | Unic & Unic{
        <>[21,250]
        & aoo
      }
    '''
    
    TryPair = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|aoo|doo|doc|daoc|vp1dd)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|doo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                | Drawdown[1:,10:,20:10]
                | Since{Max&index[0]}
                | Drawup[1:,10:,20:10]
                | Since{Min&index[0,10]}
              )
            & Since[21:, 125:, 250:]
          )
        | (
            <> Volatility[60:]
            | Volatility[ 20:]
            & (
                <>Drawdown[20:]
                | Since{Max & index[10]}
                | Since{Min & index[10]}
              )
            & Since[21:, 125:, 250:]
          )
      )
#<>#
    <>~Market & (
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|vp1dd)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
      )
#<>#
0
#<>#
    <>0
    | Corr & Corr{
        <>[21,250]
        & aoo
      }
    | Unic & Unic{
        <>[21,250]
        & aoo
      }
    '''
    
    IKGAPair = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
#<># 0 #<># 0 #<>#
    <>0
    | Corr & Corr{
        <>[21,250]
        & aoo
      }
    | Unic & Unic{
        <>[21,250]
        & aoo
      }
    '''
    
    IKGAPairDiff = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
#<>#
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:]
                | Since{Max&index[0]}
                | Since{Min&index[0,10]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
#<># 0 #<>#
    <>0
    | Corr & Corr{
        <>[21,250]
        & aoo
      }
    | Unic & Unic{
        <>[21,250]
        & aoo
      }
    '''
    
    SimplePair = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
      )
    |
        <>AssetEnc{InUni}
#<>#
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|daoc)
            & index[0,1,2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
      )
    |
        <>AssetEnc{InUni}
#<># 0 #<>#
    <>Unic{.&[21,62,250]&aoo}
    '''
    
    pZing = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|doo)
            & index[0,1,2, 0:1,1:2]
          }
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|oo{.&[10:]})}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[10:,20:]
                | Since{Min&index[20]}
              )
            & Since[21:, 250:]
          )
        | (
            <>Return{dd} & VP[1:, 10:]
            & (
                | Since{Max & index[0]}
                | Drawup[20:,20:10]
                | Since{Min & index[0]}
              )
            & Since[ 62:, 250:]
          )
      )
    | Market{.&
        <>( Weight)
        & (Return| Volatility)
        & [5:]
      }
    |
        <>Return{pure&~dd} & VP[60:]
        | FracRec[62:]
    |
        | Return{rr| af}
#<>#
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|daoc)
            & index[0,1,2, 0:1,1:2,0:2]
          }
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo)
            & [18:,9:6,15:12,18:15,12:6,18:12,15:6,18:6,21:9,18:3]
          }
      )
#<>#
0
#<>#
    <>0
    | Corr & Corr{
        <>[21,62]
        & (aoo|aooTEN)
      }
    '''
    
    ######################################## JUST SMALLER SUBSETS ##########################################################
    Short = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.&
            <>(oo|cc|aoo|acc|doo|dcc|doc|daoc|vp1dd)
            & index[0,1,2, 0:1,1:2,0:2]
          }
      )'''
    Five = '''
    <>~Market&(
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|doo|vp1dd|vp5dd|Volatility)
            & [5:,10:,15:,10:5,15:10,20:15,15:5,20:10,20:5]
          }
      )'''
    Three = '''
    <>~Market&(
        | Return{.&pure&~index} & ~Since & Return{.&
            <>(oo|aoo|doo|vp1dd|vp5dd|Volatility)
            & [3:,6:,9:,12:,15:,18:,6:3,9:6,12:9,15:12,18:15,21:18,9:3,12:6,\
            15:9,18:12,21:15,12:3,15:6,18:9,21:12,15:3,18:6,21:9,18:3,21:6,21:3]
          }
      )'''
    DrawReturn = '''
    <>~Market&(
        | (
            <>Return{(oo{.&[1:]}|aoo[1:]|doo[1:]|oo{.&[10:]}|aoo[10:]|doo[10:])}
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Max&index[0,5,10,20]}
                | Drawup[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Min&index[0,5,10,20]}
              )
            & Since[21:,62:,125:,250:]
          )
      )'''
    DrawVP = '''
    <>~Market&(
        | (
            <>Return{dd} & VP[1:, 5:, 10:]
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max}
                | Drawdown[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Max & index[0,5,10,20]}
                | Drawup[1, 5:,10:,20:, 10:5,20:10]
                | Since{Min & index[0,5,10,20]}
              )
            & Since[21:,62:,125:,250:]
          )
      )'''
    DrawVolatility = '''
    <>~Market&(
        | (
            <> Volatility[20:,60:]
            | Volatility[10:,20:]
            & (
                <>Drawdown[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Max & index[0,5,10,20]}
                | Drawup[1:, 5:,10:,20:, 10:5,20:10]
                | Since{Min & index[0,5,10,20]}
              )
            & Since[21:,62:,125:,250:]
          )
      )
      '''
    Market = '''
    | Market{.&
        <>(~Weight|Weight)
        & (Return|VP|Volatility)
        & [1:,5:,10:,20:,60:]
      }
    '''
    
############################################# MIXED GUYS #####################################################
_tp = f'Return{{oo|cc|aoo|acc|doc|daoc|vp1dd}}&({TP.Five}|{TP.Short})'
TP.PairFiveShortVP1_1_0_0_NoCorr = ''.join(f'0|{_tp*i}#<>#' for i in [1,0,0])+'0'
#TP.PairFiveShortVP1_1_0_0_NoCorr = ''.join(f'0|{_tp*i}#<>#' for i in [1,0,0])+'Corr{.&'
    
    
    
for name in TP:
    TP[name] = f'<{name}>'+TP[name]
    
def check_bank_integrity(*, F, P):
    from features import Features
    bigF = Features(F=F,P=P)
    for x in TP:
        f, q = bigF.query_solo(TP[x])