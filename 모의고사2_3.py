#신수민
def func_a(arr,num):
    ret=[]
    for i in arr:
        if i!=num:
            ret.append(i)
    return ret
def func_b(a,b):
    if a>b:
        return a-b
    else:
        return b-a

def func_c(arr):
    ret=-1
    for i in arr:
        if ret<i:
            ret=i
    return ret

def solution(visitor):
    max_first=func_c(visitor)
    visitor_removed=func_a(visitor,max_first)
    max_second=func_c(visitor_removed)
    answer=func_b(max_first,max_second)
    return answer

visitor=[1,3,2,4,5,3,6,3,7,4,5,7]
ret=solution(visitor)
print(ret)