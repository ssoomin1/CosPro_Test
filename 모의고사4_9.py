#신수민
def solution(arr,k):
    answer=0 #방 개수
    for i in arr:
        answer+=i//k
        if i%k!=0:
            answer+=1
    return answer

arr=[13,16,9,2,10,7]
k=4
ret=solution(arr,k)
print(ret)