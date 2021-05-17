#신수민
def solution(x,y):
    answer=0.0
    b1=y-x
    b2=y+x
    a1=(y*(x-(-b1)))/2.0 #y=x+b1에서 y=0일 때 x 값 : -b1
    a2=(y*(b2-x))/2.0 #y=0x+b2에서 y=0일 때 x값 : b2
    answer=a1+a2
    return answer

ret=solution(10,4)
print(ret)