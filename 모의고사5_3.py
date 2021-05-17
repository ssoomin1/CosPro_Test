#신수민
#N개 목재들 중에 재단 가능한 목재 return
def func_a(a,length):
    for i in range(len(a)):
        if a[i]>=length:
            return i #가능
    return -1 #불가능

def solution(N,orders):
    # 목재 그대로
    material = [8 for i in range(N)]
    k=0 #현재 재단 중인 목재
    price=0 #가격
    for o in orders:
        k=func_a(material,o)
        if k>=0:
            material[k]-=o
            price+=3000*o
    return price

orders=[1,3,5,7,8]
ret=solution(8,orders) #목재 그대로
print(ret)