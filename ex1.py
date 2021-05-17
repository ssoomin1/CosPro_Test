#2209신수민
a=2*(3**(1+2))
b=3**4/(2+2)
c=7//4+1**5

print(a)
print(b)
print(c)

money=int(input("금액을 입력하세요(천원보다 작게)"))
print("500원 동전의 개수 : ",money//500)
print("100원 동전의 개수 : ",(money%500)//100)