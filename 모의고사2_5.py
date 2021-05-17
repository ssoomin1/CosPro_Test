#신수민
def func_a(arr):
    counter=[0 for _ in range(1001)]
    for i in arr:
        counter[i]+=1
    return counter

def func_b(arr):
    ret=0
    for i in arr:
        if ret<i:
            ret=i
    return ret
def func_c(arr):
    ret=func_b(arr)
    for i in arr:
        if 0<i<ret:
            ret=i
    return ret

def solution(arr):
    counter=func_a(arr)
    max_cnt=func_b(counter)
    min_cnt=func_c(counter)
    return max_cnt//min_cnt

arr=[1,2,3,1,1,2,1,2,1,2,3,1,1,1,1,1]
ret=solution(arr)
print(ret)