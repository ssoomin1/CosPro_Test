#2209 신수민
import random
n=int(input("값을 입력하세요: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("1부터",n,"까지의 합:",sum)

c_num=random.randint(1,10)
check=0

while(True):
    num = int(input("컴퓨터가 생각한 수를 맞춰보세요(1~10사이) >> "))
    check+=1
    if num>c_num:
        print("입력한 수가 큽니다.")
    elif num<c_num:
        print("입력한 수가 작습니다.")
    else:
        print(check,"번만에 맞췄습니다.")
        break