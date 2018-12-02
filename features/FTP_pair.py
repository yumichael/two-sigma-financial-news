from common import *

copyTemplate = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.& =.55
            <>(oo?.6|cc?.6|aoo?.3|acc?.3|doo?.3|dcc?.3|doc?.3|daoc?.3|vp1dd?.5)
            & index[0?.7,1?.7,2?.7, 0:1?.7,1:2?.7,0:2?.7] @index
          }
        | Return{.&pure&~index} & ~Since & Return{.& =.6 *five
            <>(oo?.7|aoo?.5|doo?.3|vp1dd?.4|vp5dd?.6|Volatility?.4)
            & [5:?.5,10:?.7,15:?.6,10:5?.5,15:10?.5,20:15?.5,15:5?.7,20:10?.7,20:5?.6] @med
          }
        | Return{.&pure&~index} & ~Since & Return{.& =.6 *three
            <>(oo?.7|aoo?.5|doo?.3|vp1dd?.4|vp5dd?.6|Volatility?.4)
            & [3:?.4,6:?.5,9:?.6,12:?.7,15:?.6,18:?.5,6:3?.4,9:6?.4,12:9?.4,15:12?.4,18:15?.4,21:18?.4,9:3?.5,12:6?.5,\
            15:9?.5,18:12?.5,21:15?.5,12:3?.6,15:6?.6,18:9?.6,21:12?.6,15:3?.7,18:6?.7,21:9?.7,18:3?.6,21:6?.5,21:3?.5] @med
          }
        | ( =.53
            <>Return{(oo{.&[1:]}?.8|aoo[1:]?.2|doo[1:]?.2|oo{.&[10:]}?.6|aoo[10:]?.2|doo[10:]?.2)} @smooth
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max} =.5
                | Drawdown[1:?.5, 5:?.4,10:?.6,20:?.5, 10:5?.4,20:10?.6] @medlong
                | Since{Max&index[0?.7,5?.2,10?.2,20?.2]} =.5 @medlong
                | Drawup[1:?.2, 5:?.1,10:?.2,20:?.2, 10:5?.1,20:10?.2] =.3 @medlong
                | Since{Min&index[0?.6,5?.2,10?.3,20?.2]} @medlong
              )
            & Since[21:?.5, 62:?.7, 125:?.3, 250:?.3] @long
          )
        | ( =.25
            <>Return{dd} & VP[1:?.3, 5:?.5, 10:?.5] @smooth
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max} =.7
                | Drawdown[1:?.35, 5:?.2,10:?.2,20:?.2, 10:5?.2,20:10?.35] =.5 @medlong
                | Since{Max & index[0?.7,5?.2,10?.35,20?.2]} @medlong
                | Drawup[1?.5, 5:?.2,10:?.3,20:?.5, 10:5?.2,20:10?.3] =.6 @medlong
                | Since{Min & index[0?.7,5?.2,10?.35,20?.25]} @medlong
              )
            & Since[21:?.15, 62:?.25, 125:?.5, 250:?.6] @long
          )
        | ( =.3
            <> Volatility[20:?.5, 60:?.2] =.7 @long
            | Volatility[10:?.6, 20:?.6]
            & (
                <>Drawdown[1:?.4, 5:?.3,10:?.2,20:?.2, 10:5?.3,20:10?.2] =.4 @medlong
                | Since{Max & index[0?.3,5?.3,10?.5,20?.1]} =.8 @medlong
                | Drawup[1:?.4, 5:?.3,10:?.2,20:?.2, 10:5?.3,20:10?.2] =.4 @medlong
                | Since{Min & index[0?.3,5?.3,10?.5,20?.1]} =.8 @medlong
              )
            & Since[21:?.1, 62:?.2, 125:?.5, 250:?.5] @long
          )
      )
    | Market{.& =.5
        <>(~Weight?.5 | Weight?.5)
        & (Return?.7 | VP?.5 | Volatility?.5)
        & [1:?.4,5:?.3,10:?.4,20:?.5,60:?.4] @short @med @long
      }
    | =.2
        <>Return{pure&~dd} & VP[1:?.2,5:?.1,10:?.2,20:?.1,60:?.1] =.6 @short @med @long
        | FracRec[21:?.5,62:?.3,125:?.1,250:?.3] =.7 @long
    | =.25
        <>AssetEnc{InUni} =1.
        | AssetEnc{Code} =.0
    | =.1
        <>FaceValue{Volume?.6 | Open?.5 | Close?.5} = .3
        | Return{mix[1?.5,2?.5,3?.5,4?.5,5?.5,6?.5,7?.5,8?.5,9?.5,11?.5,12?.5,13?.5,14?.5,15?.5,16?.5,17?.5,18?.5,19?.5]}=.6
        | Return{rr?.5 | af?.5 | it?.5} =.8
    | =.15
        Time{long?.9 | short?.5}
'''

class copyEdit(metaclass=staticclass):
    def _item_(x):
        return x*.9
    
    def long(y, *, e):
        care = [21, 62, 125, 250]
        ssets = [[21],[62],[125],[250],[21,62],[125,250],[62,250],[21,125],[21,250],[21,125,250],[21,62,250],[21,62,125,250]]
        if __class__._random_data[0] < .3: # cancel 
            return y
        sset = ssets[math.floor(len(ssets)*__class__._random_data[1])]
        if any(str(n) in e for n in sset):
            return 1.
        elif any(str(n) in e for n in care):
            return -1.
        else:
            return y
    
    def five():
        return __class__._random_data[2] - .42
    def three():
        return .42 - __class__._random_data[2]

diffTemplate = '''
    <>~Market & (
        <>Return{.&pure&~digit&~TEN} & ~Since & Return{.& =.65
            <>(oo?.6|cc?.6|aoo?.3|acc?.3|doo?.3|dcc?.3|doc?.3|daoc?.3|vp1dd?.5)
            & index[0?.7,1?.7,2?.7, 0:1?.7,1:2?.7,0:2?.7] @index
          }
        | Return{.&pure&~index} & ~Since & Return{.& =.65 *five
            <>(oo?.7|aoo?.5|doo?.3|vp1dd?.4|vp5dd?.6|Volatility?.4)
            & [5:?.5,10:?.7,15:?.6,10:5?.5,15:10?.5,20:15?.5,15:5?.7,20:10?.7,20:5?.6] @med
          }
        | Return{.&pure&~index} & ~Since & Return{.& =.65 *three
            <>(oo?.7|aoo?.5|doo?.3|vp1dd?.4|vp5dd?.6|Volatility?.4)
            & [3:?.4,6:?.5,9:?.6,12:?.7,15:?.6,18:?.5,6:3?.4,9:6?.4,12:9?.4,15:12?.4,18:15?.4,21:18?.4,9:3?.5,12:6?.5,\
            15:9?.5,18:12?.5,21:15?.5,12:3?.6,15:6?.6,18:9?.6,21:12?.6,15:3?.7,18:6?.7,21:9?.7,18:3?.6,21:6?.5,21:3?.5] @med
          }
        | ( =.25
            <>Return{(oo{.&[1:]}?.8|aoo[1:]?.2|doo[1:]?.2|oo{.&[10:]}?.6|aoo[10:]?.2|doo[10:]?.2)} @smooth
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max} =.5
                | Drawdown[1:?.5, 5:?.4,10:?.6,20:?.5, 10:5?.4,20:10?.6] @medlong
                | Since{Max&index[0?.7,5?.2,10?.2,20?.2]} =.5 @medlong
                | Drawup[1:?.2, 5:?.1,10:?.2,20:?.2, 10:5?.1,20:10?.2] =.3 @medlong
                | Since{Min&index[0?.6,5?.2,10?.3,20?.2]} @medlong
              )
            & Since[21:?.5, 62:?.7, 125:?.3, 250:?.3] @long
          )
        | ( =.25
            <>Return{dd} & VP[1:?.3, 5:?.5, 10:?.5] @smooth
            & (
                <> ~Drawdown&~Drawup&~Since{Min}&~Since{Max} =.7
                | Drawdown[1:?.35, 5:?.2,10:?.2,20:?.2, 10:5?.2,20:10?.35] =.5 @medlong
                | Since{Max & index[0?.7,5?.2,10?.35,20?.2]} @medlong
                | Drawup[1?.5, 5:?.2,10:?.3,20:?.5, 10:5?.2,20:10?.3] =.6 @medlong
                | Since{Min & index[0?.7,5?.2,10?.35,20?.25]} @medlong
              )
            & Since[21:?.15, 62:?.25, 125:?.5, 250:?.6] @long
          )
        | ( =.25
            <> Volatility[20:?.5, 60:?.2] =.7 @long
            | Volatility[10:?.6, 20:?.6]
            & (
                <>Drawdown[1:?.4, 5:?.3,10:?.2,20:?.2, 10:5?.3,20:10?.2] =.4 @medlong
                | Since{Max & index[0?.3,5?.3,10?.5,20?.1]} =.8 @medlong
                | Drawup[1:?.4, 5:?.3,10:?.2,20:?.2, 10:5?.3,20:10?.2] =.4 @medlong
                | Since{Min & index[0?.3,5?.3,10?.5,20?.1]} =.8 @medlong
              )
            & Since[21:?.1, 62:?.2, 125:?.5, 250:?.5] @long
          )
      )
    | =.2
        | FracRec[21:?.5,62:?.3,125:?.1,250:?.3] @long
    | =.1
        <>Return{mix[1?.5,2?.5,3?.5,4?.5,5?.5,6?.5,7?.5,8?.5,9?.5,11?.5,12?.5,13?.5,14?.5,15?.5,16?.5,17?.5,18?.5,19?.5]}=.6
        | Return{rr?.5 | af?.5 | it?.5} =.8
'''

class diffEdit(metaclass=staticclass):
    def _item_(x):
        return x*.96
    
    def long(y, *, e):
        care = [21, 62, 125, 250]
        ssets = [[21],[62],[125],[250],[21,62],[125,250],[62,250],[21,125],[21,250],[21,125,250],[21,62,250],[21,62,125,250]]
        if __class__._random_data[0] < .3: # cancel 
            return y
        sset = ssets[math.floor(len(ssets)*__class__._random_data[1])]
        if any(str(n) in e for n in sset):
            return 1.
        elif any(str(n) in e for n in care):
            return -1.
        else:
            return y
    
    def five():
        return __class__._random_data[2] - .42
    def three():
        return .42 - __class__._random_data[2]
    
corrTemplate = '''
    <>0
    | Corr & Corr{ =.95
        <>[10?.5,21?.7,62?.6,250?.7]
        & ay[1?.7,10?.6,20?.5]
      }
'''

class corrEdit(metaclass=staticclass):
    pass