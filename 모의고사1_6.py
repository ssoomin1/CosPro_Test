#신수민 ws 어렵다. 공부할 것
def solution(left_rings):
    answer=0
    for i in range(len(left_rings)):
        if left_rings[i]<=i: #왼쪽 고리가 오른쪽 고리보다 크거나 같은 경우
            for k in range(i): #고리값 k<i(왼쪽 고리번호)에서
                #i가 연결된 값보다 k가 연결된 값이 크면 교차
                if left_rings[k]>left_rings[i]:
                    answer+=1
    return answer

#0-0 / 1-3 /2-1 / 3-4 /4-2
leftrings=[0,3,1,4,2]
ret=solution(leftrings)
print(ret)