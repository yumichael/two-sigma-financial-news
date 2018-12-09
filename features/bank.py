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
    
    InitKaggleGo = '''
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
        <>[10,21,250]
        & ay[1]
      }
    | Corr{Uni}
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
        & ay[1]
      }
    | Corr{Uni}
    '''
    
    IKGPair = '''
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
#<># 0 #<># 0 #<>#
    <>0
    | Corr & Corr{
        <>[21,62,125,250]
        & ay[1,10]
      }
    | Corr{Uni}
    '''
    
    IKGPairDiff = '''
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
    |
        <>AssetEnc{InUni}
        | AssetEnc{Code}
    |
        <>FaceValue{Volume}
        | Return{mix[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]}
        | Return{rr|af|it}
#<># 0 #<>#
    <>0
    | Corr & Corr{
        <>[21,62,125,250]
        & ay[1,10]
      }
    | Corr{Uni}
    '''