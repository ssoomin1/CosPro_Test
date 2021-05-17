#2209 신수민
x=15
if x>10 and x<20:
    print("조건에 맞습니다.")

a=int(input("첫번째 정수를 입력하세요: "))
b=int(input("두번째 정수를 입력하세요: "))
c=int(input("세번째 정수를 입력하세요: "))

if a>b and a>c:
    print("가장 큰 수:",a)
elif b>c and b>a:
    print("가장 큰 수:", b)
else:
    print("가장 큰 수:", c)
