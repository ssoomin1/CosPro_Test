#신수민
def solution(positive,negative):
    answer=[0,0] #전체학생 수 , 찬성, 반대
    p_total=0
    n_total=0
    p_student=0
    n_student=0

    for i in range(4):
        for j in range(3):
            p_total+=positive[i][j]
            n_total+=negative[i][j]
    p_student= int(p_total / (p_total+n_total) *100)
    n_student=int(n_total/(p_total+n_total)*100)
    answer[0]=p_student
    answer[1]=n_student
    return answer

positive=[[3,2,7],[4,2,6],[5,3,8],[7,6,8]]
negative=[[30,50,120],[70,90,180],[120,150,260],[102,120,104]]
print(solution(positive,negative))