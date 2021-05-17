#신수민
def solution(word):
    num2alpha=["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
    answer='' #숫자로 변환한 전화번호 저장할 변수
    for c in word:  #소문자로 이뤄진 전화번호 문자열 검사
        for i in range(len(num2alpha)): #0~9까지 해당 숫자의 문자 검사
            for a in num2alpha[i]: #i위치에 문자열인지 검사
                if a==c: #전화번호 문자열과 문자열 비교
                    answer+=str(i)
                    break #3개중에ㅐ 하나만 같아도 됨
    return answer

word='whitepawn' #941837296
ret=solution(word)
print(ret)