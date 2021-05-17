#신수민
def solution(price,money):
    answer=0
    for p in price:
        money-=p
    answer=money
    if answer<0:
        answer=-1
    return answer

price=[2100,3200,2100,800]
money=10000
ret=solution(price,money)
print(ret)