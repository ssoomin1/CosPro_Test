#신수민
def solution(scores):
    result=[0,0,0,0] #A,B,C,D
    for i in range(4):
        for k in range(4):
            if i!=k:  #같으면 자기 자신과 싸움이 되기 때문에 같지않을때
                result[i]+=scores[i][k]*2
                #승 2점, 패 0점 승점 계산
    return result

scores=[
    [0,1,1,1],
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0]]

print(solution(scores))