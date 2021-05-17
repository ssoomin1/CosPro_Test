#2209 신수민
data1=[i for i in range(1,10+1)]
data2=[i for i in range(1,10+1) if i%3==0]

num=0
for i in data1:
    for j in data2:
        if i==j:
            num+=1
print("같은 데이터의 개수: ",num)
