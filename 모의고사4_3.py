#신수민
def solution(student,apts):
    result=0
    total=0
    for s in student:
        total+=s
    result=total//12
    if total%12 !=0 :
        result+=1
    return result

student=[2,5,4,7,8,2]
ret=solution(student,len(student))
print(ret)