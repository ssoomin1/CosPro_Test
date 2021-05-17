#신수민
def solution(n,m):
    answer=0
    OPEN,CLOSE=0,1
    room=[CLOSE for i in range(m+1)] #처음 모든 문은 닫힘
    for i in range(1,n+1): #잔 수
        for k in range(1,m+1): #교실
            if k%i==0: #교실 번호가 술잔 수의 배수일 경우
                #room[k]= 0 if room[k]==1 else 1 #1->0 0->1
                room[k]=1-room[k]
    answer=room.count(OPEN)
    return answer

n=10 #술
m=20 #교실
ret=solution(n,m)
print(ret)