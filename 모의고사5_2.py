#신수민
def solution(arr):
    answer=0
    for i in range(len(arr)):
        price=arr[i]
        if (i+1) % 4==0: #인덱스는 0번부터이기 때문에
            price=price*0.5 #price//2
        answer+=price
    return answer
arr=[100,500,200,400,300]
ret=solution(arr)
print(ret)