#신수민
def solution(name_list):
    answer=0
    for name in name_list:
        for char in name:
            if char.find('A') != -1 or char.find('K') != -1:
                answer+=1
                break
    return answer

names=['Adios','Kickboard Association','google']
ret=solution(names)
print(ret)