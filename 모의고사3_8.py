#신수민
def solution(password,key):
    answer=0
    match_cnt=0 #키가 있는지 카운트
    for k in key:
        for p in password:
            if k==p:
                match_cnt+=1
                break
    if match_cnt>=len(key):
        answer=1
    return answer

password="12341sa korea uk"
key="k 1 u"
ret=solution(password,key)
print(ret)