#신수민
def solution(a,b):
    amswer=0
    diff=a-b if a>b else b-a
    answer=10/diff
    return answer*60

a=10
b=12
ret=solution(a,b)
print(ret)