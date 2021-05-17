#신수민
def func_a(a): #4자리 시간 천&백 자리=시간 십&일=분
    #4자리 a//100 몫은 시간, a%100 분
    return ((a//100)*60)+(a%100)

def solution(arr):
    answer=0
    min_a=func_a(2200) #밤 10시일경우 분 계산 => 마감시간
    for i in arr: #계산할 주차차량
        min_b=func_a(i) #주차장 진입시간
        elapsed_minute=min_a-min_b #주차장에 머무른 시간
        answer+=1000+(elapsed_minute//10)*500
    return answer

arr=[2030,1600]
ret=solution(arr)
print(ret)

