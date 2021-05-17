#신수민
def solution(wats,bill):
    result=[0 for _ in range(8)] #세대별 전기요금
    unit_price=int(bill/wats[0])+1 #단위요금 = 합 / 총 사용량
    for i in range(len(wats)-1):
        result[i]=wats[i+1]*unit_price #단위요금 * 사용량 = 전기요금
    return result

bill=1275
wat=[10,20,60,30,10,20,60,30]
t=0
for i in wat:
    t+=i
wats=[t]+wat #리스트합치기(총합 추가)
print("사용량: ",wats)
ret=solution(wats,bill)
print("전기요금 :",ret)