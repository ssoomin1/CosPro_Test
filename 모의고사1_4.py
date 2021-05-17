#신수민
def solution(price,grade):
    answer=0
    if grade=="S":
        answer=int(price*1.05)
    elif grade=="G":
        answer=int(price*1.1)
    elif grade=="V":
        answer=int(price*1.15)
    return answer
price=1300
grade="G"
ret=solution(price,grade)
print(ret)