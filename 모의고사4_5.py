#신수민
def func_a(s):
    answer=False
    cnt=0
    for i in s:
        if i =='[':
            cnt+=1
        if i==']':
            cnt-=1
    if cnt==0 :  #쌍이 맞는 경우
        answer=True
    return answer

def solution(string):
    answer=0
    #not이 있기 때문에 return값은 False나 True
    if not func_a(string):
        return -1
    for i in string:
        if i==']':
            answer+=1
    return answer

string="[[][]]"
ret=solution(string)
print(ret)