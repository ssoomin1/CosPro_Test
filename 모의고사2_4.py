#신수민
def solution(scores):
    grade_counter=[0 for i in range(5)]
    for i in scores:
        if i>=85:
            grade_counter[0]+=1
        elif i>=70:
            grade_counter[1]+=1
        elif i>=55:
            grade_counter[2]+=1
        elif i>=40:
            grade_counter[3]+=1
        else:
            grade_counter[4]+=1
    return grade_counter
scores=[10,20,30,40,50,60,70,80,90,100]
ret=solution(scores)
print(ret)