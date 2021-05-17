#신수민
def func_a(a): #a리스트에서 min값
    min=a[0]
    for i in a:
        if i<min:
            min=i
    return min

def solution(price):
    sales=[0 for _ in range(4)]
    k=0
    for i in price:  #for i in range(len(price)):
        if i[0]<5000:  #if price[i][0] < 5000:
            percent=0.25
        elif i[0]<15000:
            percent=0.20
        elif i[0]<100000:
            percent=0.15
        else: percent=0.1
        #sales[price,index(i)]
        sales[k]=int(i[0]*percent*i[1])
        k+=1
    return func_a(sales)

price=[
    [50000,10],
    [15000,20],
    [5000,40],
    [150000,100]
]
ret=solution(price)
print(ret)