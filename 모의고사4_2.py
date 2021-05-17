#신수민
def func_a(arr):
    total=0
    for i in arr:
        total+=i
    return total

def solution(arr,payload):
    answer=0
    sum=func_a(arr)   #제공한 추의 무게들의 합
    if sum>=payload:  #추의 무게를 잴 수 있다면
        arr.sort()   #추 오름차순
        arr.reverse()  #큰 추부터 다시 재정렬(추 개수를 적게 하기 위해_
        weight=0 #추의 무게를 저장할 변수
        for i in range(len(arr)): #추의 개수만큼 반복
            diff=payload-weight #구슬 무게에 추의 무게로 재기(뺄셈)
            if arr[i]<=diff: #추를 더 올릴 수 있으면(덜 잰 경우)
                weight+=arr[i] # 추 무게합
                answer+=1 #추가된 추 카운터 
        if weight != payload: #남은 추로 무게를 잴 수 없는 경우
            answer=0
    return answer
            
arr=[2,3,5,7,13,17,19,23]
#46,45도 해보기
payload=25
ret=solution(arr,payload)
print("추 개수:",ret)