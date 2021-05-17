#신수민
def solution(string):
    answer=0
    number=0
    s=string+' ' #마지막 문자가 숫자인 경우 더해지지않기 때문에 추가
    for c in s:
        if c>='0' and c<='9':
            number=number*10+int(c) #연속 숫자인 경우 자리수맞추기
        else: #숫자 다음 문자가 올 경우 answer에 number를 더함
            answer+=number
            number=0
    return answer

string="12 korean34 usa10"
ret=solution(string)
print(ret)