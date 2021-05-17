#신수민
def solution(weight,k):
    answer=0
    for w in weight:
        if w>k:
            answer+=1
    return answer

weights=[65,70,75,80,84]
ret=solution(weights,70)
print(ret)