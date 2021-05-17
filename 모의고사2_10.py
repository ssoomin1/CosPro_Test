#신수민
def sum_isbn(isbn):
    sum=0
    for i in range(len(isbn)):
        c=int(isbn[i])
        if i%2:
            w=3
        else:
            w=1
        sum+=w*c
    return sum

def solution(isbn):
    answer=''
    total=sum_isbn(isbn[:-1])
    a=10-(total%10)
    if a==10:
        answer='0'
    else:
        answer=str(a)
    return answer

isbn='978897058122'
ret=solution(isbn)
print(ret==isbn[-1])