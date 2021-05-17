#신수민_13
def func_a(arr,n):
    ret=[]
    for x in arr:
        if x!=n:
            ret.append(x)
    return ret
def func_b(a,b):
    if a>=b:
        return a-b
    else:
        return b-a
def func_c(arr):
    ret=-1
    for x in arr:
        if ret<x:
            ret=x
    return ret
def solution(scores):
    max_first=func_c(scores)
    visitor_removed=func_a(scores,max_first)
    max_second=func_c(visitor_removed)
    answer=func_b(max_first,max_second)
    return answer

visitor=[50,20,30,10,40]
ret=solution(visitor)
#print(ret)

#신수민_14
def solution(scores):
    grade_counter=[0 for i in range(5)]
    for x in scores:
        if 85<=x<=100:
            grade_counter[0]+=1
        elif 70<=x:
            grade_counter[1]+=1
        elif 55<=x:
            grade_counter[2]+=1
        elif 40<=x:
            grade_counter[3]+=1
        else: grade_counter[4]+=1
    return grade_counter

scores=[50,95,70,65,90,80,60]
ret=solution(scores)
#print("solution 함수의 반환 값은",ret,"입니다.")

#신수민_15
def solution(stones):
    cnt=0 #점프카운트
    current=0 #스톤위치 (index)
    n=len(stones) #총 스톤 개수

    while(current<n):
        current+=stones[current]
        cnt+=1
    return cnt

st=[2,5,1,3,2,1]
#print(st)
#print(solution(st))

#신수민_16
def solution(height,k):
    answer=0
    n=len(height)
    for h in height:
        if h>k:
            answer+=1
    return answer

h=[165,170,175,180,184]
print(solution(h,170))

#신수민_17
def solution(s): #str아이템 수정 불가(할당 불가)
    s_lst=list(s)  #문자열을 리스트로 변경해서 수정
    n=len(s)
    for i in range(n):
        if s_lst[i]=='a':
            s_lst[i]='z' #리스트아이템 변경 가능
        elif s_lst[i]=='z':
            s_lst[i]='a'
    return "".join(s_lst)
str="abzzaabba"
print(solution(str))

#신수민_18
def solution(name_list):
    answer=0
    for name in name_list:
        for n in name:
            if n=='j' or n=='k':
                answer+=1
                break
    return answer

names=["james","kim john","jokin","jack","soomin"]
ret=solution(names)
print(ret)

#신수민_19
def solution(price,money):
    answer=0
    total=0
    for p in price:
        total+=p
    answer=money-total
    if answer<0:
        answer=-1
    return answer

price=[2100,3200,2100,800]
money=10000
print("지불금액:",money)
print("잔액:",solution(price,money))

#신수민_20
def solution(arr,k):
    answer=0
    arr_list=[]
    for i in arr:
        for j in i:
            arr_list.append(j)
    arr_list.sort()
    answer=arr_list[k-1]
    return answer

arr=[[5,12,4,31],
     [54,13,11,2],
     [43,44,19,26],
     [33,65,20,21]]
print(solution(arr,4))