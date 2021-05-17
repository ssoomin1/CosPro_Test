#신수민
def solution(a,b):
    result=[0,0] #0 : 스트라이크  1: 볼
    for i in range(3):
        temp=b
        for k in range(3):
            if a%10==temp%10:
                if i==k:
                    result[0]+=1
                else:
                    result[1]+=1
            temp//=10
        a//=10
    return result

a,b=123,345
ret=solution(a,b)
print(ret)