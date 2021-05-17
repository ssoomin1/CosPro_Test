#신수민
def solution(shoes_size):
    answer=[]
    answer=[0 for _ in range(6)]
    for s in shoes_size:
        if s=="7":
            answer[0]+=1
        elif s=="7.5":
            answer[1]+=1
        elif s=="8":
            answer[2]+=1
        elif s=="8.5":
            answer[3]+=1
        elif s=="9":
            answer[4]+=1
        elif s=="9.5":
            answer[5]+=1
    return answer
shoes_size=["7","7.5","8","8.5","9","9.5"]
ret=solution(shoes_size)
print(ret)