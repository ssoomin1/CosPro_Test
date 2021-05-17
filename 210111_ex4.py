#2209 신수민
def multiple(n,m):
    result=0
    for i in range(1,m+1):
        result=n**i
    return result

fnum=int(input("첫 번째 정수를 입력하세요>> "))
snum=int(input("두 번쨰 정수를 입력하세요>> "))
res=multiple(fnum,snum)
print(fnum,"를",snum,"번 곱한 결과는 ",res)