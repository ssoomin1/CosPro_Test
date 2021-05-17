#신수민
def solution(number):
    count=0
    for i in range(1,number+1):
        current=i
        while current !=0:
            unit=current%10 #일의 자리 뗴기
            if unit==3 or unit==6 or unit==9:
                count+=1
            current//=10 #일의 자리 버리기(자릿수 내림)
    return count

number=36
ret=solution(number)
print(ret)