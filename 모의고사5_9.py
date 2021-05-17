#신수민
def solution(answer):
    min=1
    max=100
    result=0
    for i in answer:
        result=(max+min)/2 #중간값
        if min==max or i=='c':
            break #끝까지 검색했거나 답을 찾았거나
        if i=='u': #답보다 큰 경우 틀림: 왼쪽검사
            max=result #max변경필요
        if i=='d': #오른쪽검사
            min=result #min변경필요
    return int(result)

answer='udduduudc'
ret=solution(answer)
print(ret)