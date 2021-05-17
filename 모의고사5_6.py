#신수민
def solution(down,up):
    answer=0 #최대 입석
    passenger=0
    n=len(up) #승차역 수
    for i in range(n):
        passenger+=up[i]-down[i]
        stand=passenger-240 #240개 좌석중 입석 검사
        if stand<0 : #입석이 없을 경우
            stand=0
        if stand>0 and stand>answer:
            answer=stand #최대 입석 수 저장
    return answer

up=[240,100,0,160,10,140]
down=[0,0,140,80,0,0]
ret=solution(down,up)
print(ret)