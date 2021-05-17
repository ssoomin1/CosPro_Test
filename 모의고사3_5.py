#신수민
def solution(mho_cards,mhe_cards):
    result=-1
    mho_check=0
    mhe_check=0
    for i in range(13):
        if mho_cards[i]>mhe_cards[i]:
            mho_check+=1
        elif mhe_cards[i]>mho_cards[i]:
            mhe_check+=1
    if mho_check > mhe_check:
        result=1
    elif mho_check==mhe_check:
        result=-1
    elif mho_check < mhe_check:
        result=0
    return result

mho_cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]
mhe_cards=[2,1,3,4,5,9,6,7,8,10,11,12,13]
ret=solution(mho_cards,mhe_cards)
print(ret)