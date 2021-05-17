#신수민
def func_a(a):
    total=0
    for i in a:
        total+=1
    return total

def func_b(a,b):
    return b-a if a<b else a-b
def func_c(a,b):
    max_diff=0
    max_score=0
    for i in b:
        diff=func_b(a,i)
        if max_diff<diff:
            max_diff=diff
            max_score=i
    return max_score

def solution(scores):
    total=func_a(scores)
    avg=total//len(scores)
    answer=func_c(avg,scores)
    return answer

scores=[10,90,50,30,60]
ret=solution(scores)
print(ret)