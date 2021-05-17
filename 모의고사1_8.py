#신수민 이거 이상함. 
def solution(sentence):
    filtered=[]
    for s in sentence:
        if s!='' and s!='.':
            filtered.append(s)
    print(filtered)
    before=''.join(filtered)
    print("before: ",filtered)
    filtered.reverse()
    after=''.join(filtered) #리스트를 문자열로(join)
    print("after:",filtered)
    return before==after

sentence="r     ace c.a.ra"
ret=solution(sentence)
print(ret)