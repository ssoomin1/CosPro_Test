#신수민
def solution(strings):
    result=0
    for s in strings:
        length=len(s)#13//4 = 3
        result+=(length//4)
        if length%4!=0:
            result+=1 #나머지가 있을 경우에 추가가
    return result
strings=["abcdef1234567"]
ret=solution(strings)
print(ret)