#신수민
def solution(cards):
    answer=0
    for i in range(3):
        for k in range(i+1,5):
            for n in range(k+1,5):
                print(cards[i],cards[k],cards[n])
                if (cards[i]+cards[k]+cards[n])%2==1:
                    answer+=1
    return answer

cards=[7,5,6,4,9]
ret=solution(cards)
print(ret)