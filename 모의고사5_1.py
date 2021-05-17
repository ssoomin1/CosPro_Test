#신수민
def solution(arr):
    answer=0
    total=0 #총 거리
    for a in arr:
        total+=a
    #print(total)
    answer=total//40-1 #처음에 완충
    if total%40 !=0:
        answer+=1
    return answer
arr=[20,10,30,30,20,10]
ret=solution(arr)
print(ret)

