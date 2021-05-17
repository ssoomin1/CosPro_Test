#신수민
def solution(input):
    answer=0
    x=0
    y=0
    for i in input:
        if i=='w': y-=1
        elif i=='s':y+=1
        elif i=='a':x-=1
        elif i=='d':x+=1
        if x==y:answer+=1
    return answer

input="wsadsdwasd"
ret=solution(input)
print(ret)