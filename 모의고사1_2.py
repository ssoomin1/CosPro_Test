#신수민
def func_a(s):
    s.sort()
    return s[len(s)-1],s[0]

def func_b(s):
    ret=0
    for i in s:
        ret+=i
    return ret

def solution(scores):
    sum=func_b(scores)
    max,min=func_a(scores)
    return sum-max-min

scores=[10,20,50,90,30,40]
ret=solution(scores)
print(ret)