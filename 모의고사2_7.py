#신수민
def solution(s):
    answer=[]
    for c in s:
        if '0'<=c<='9':
            n=ord('i')-ord(c)
            c=chr(n)
        answer.append(c)
    return ''.join(answer)

s="ab1c3d"
ret=solution(s)
print(ret)

i=ord('i')
y=ord('0')
g=ord('9')
print(i,y,g)