#신수민
def func_a(arr):
    total=0
    for i in arr:
        total+=i
    return total

def solution(total,arr):
    result=[]
    req_total=func_a(arr)
    for i in arr:
        if req_total>total:
            result.append(total//len(arr))
        else:
            result.append(i)
    return result

total=100
arr=[20,20,30,40]
ret=solution(total,arr)
print(ret)