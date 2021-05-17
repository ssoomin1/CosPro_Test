#신수민
def solution(table):
    answer=0
    max=0
    for i in range(1,len(table)) : #행
        sum=0
        for k in range(5):
            teacher=table[0][k]
            student=table[i][k]
            if teacher==student:
                sum+=1
    if max<sum:
        max=sum
        print(i,"번 학생이 선생님과 가장 많이 같은 반")
        answer=i
    return answer

table=[
    [2,6,1,7,3],   #선생님
    [2,9,4,6,8],   #학생1
    [6,3,4,7,1],   #학생2
    [7,7,1,1,2],   #학생3
    [8,6,9,7,3],   #학생4
    [4,6,5,9,2]]   #학생5

print(solution(table))