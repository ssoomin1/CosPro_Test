#신수민
def solution(arr):
    answer=[0,0,0]
    for i in range(3): #과목
        for k in range(4): #학생
            answer[i]+=arr[i*4+k]
    return answer

arr=[8,5,3,5,6,7,3,4,5,6,7,8]
ret=solution(arr)
print(ret)