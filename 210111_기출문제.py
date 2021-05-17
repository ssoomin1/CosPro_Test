#2209 신수민
# def solution(shirt_size):
#     answer=[0,0,0,0,0,0]
#     for i in shirt_size:
#         if i=="XS":
#             answer[0]+=1
#         elif i=="S":
#             answer[1]+=1
#         elif i=="M" :
#             answer[2]+=1
#         elif i=="L" :
#             answer[3]+=1
#         elif i=="XL":
#             answer[4]+=1
#         elif i=="XXL":
#             answer[5]+=1
#
#     return answer
#
# shirt_size=["XS","S","M","L","XL","XXL"]
# ret=solution(shirt_size)
# print("solution 함수의 반환값은 ",ret,"입니다.")

#신수민
# def solution(price,grade):
# #     answer=0
# #     if grade=="S":
# #         #할인율 5
# #         answer=price*0.95
# #     elif grade=="G":
# #         answer=price*0.9
# #     elif grade=="V":
# #         answer=price*0.85
# #     return answer
# #
# # price=10000
# # answer=solution(price,"G")
# # print(answer)

#신수민_3
def func_a(month,day):
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    total=0
    for i in range(month-1): #자기 자신을 제외해야되기때문에 아직 만약 3월이라면 다 지나간 것이 아니기 때문
        total+=month_list[i]
    total+=day
    #기준일이 1월 1일인데 한번더 세어지기 때문에 -1
    return total-1

def solution(start_month,start_day,end_month,end_day):
    start_total = int(func_a(start_month,start_day))
    end_total=int(func_a(end_month,end_day))
    return end_total-start_total

start_month,start_day=1,22
end_month,end_day=2,2
ret=solution(start_month,start_day,end_month,end_day)
#print(ret)

#신수민_4
def func_a(arr):
    counter=[0 for _ in range(1001)]
    for x in arr:
        counter[x]+=1
    return counter

def func_b(arr):
    ret=0
    for x in arr:
        if ret<x:
            ret=x
    return ret

def func_c(arr):
    INF=1001 #최솟값 추리기
    ret=INF
    for x in arr:
        if x!=0 and ret>x: #x의 값은 1 이상이다.
            ret=x
    return ret

def solution(arr):
    counter=func_a(arr)
    max_cnt=func_b(counter)
    min_cnt=func_c(counter)
    return int(max_cnt//min_cnt)

#신수민_5
def solution(arr):
    left,right=0,len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

arr=[1,4,2,3]
result=solution(arr)
#print(result)

#신수민_6
def solution(number):
    count=0
    for i in range(1,number+1): #1~20
        current=i
        temp=count
        while current != 0:
            if current%10==3 or current%10==6 or current%10==9:
                count+=1
                print("짝",end='')
            current=current//10 #두자리 이상의 수일 경우
        if temp==count:  #temp == count 변화가 없을 경우
            print(i,end="")
        print(" ",end="")
    print("")
    return count

solution(20)


#신수민_7
def solution(scores):
    count=0
    for s in scores:
        if 650<=s and s<800:
            count+=1
    return count

scores=[100,200,500,700,900,600,800]
#print(solution(scores))

#신수민_8
def solution(sentence):
    str=''
    for c in sentence:
        if c!='.' and c!=' ':
            str+=c
    size=len(str)
    #펠린드롬인지 아닌지 확인하는 문장
    for i in range(size//2):
        if str[i]!=str[size-1-i]:
            return False
    return True

s="never odd or even"
print(solution(s))
s="apple banana zzz"
#print(solution(s))

#신수민_9
def solution(characters):
    result=""
    result+=characters[0]
    for i in range(1,len(characters)):
        if characters[i-1] != characters[i]:
            result+=characters[i]
    return result

#print(solution("senteeeencccccceeeee"))

#신수민_10
def sum(data):
    total=0
    for d in data:
        total+=d
    return total

def solution(data):
    total=sum(data) #총합
    average=total/len(data) #평균 = 총합 / 인원수 total/len(data)
    cnt=0
    for d in data:
        if d<=average:
            cnt+=1
    return cnt

#신수민_11
def func_a(k):
    sum=0
    for i in range(1,k+1):
        sum+=i
    return sum

def solution(n,m):
    sum_to_m=func_a(m)
    sum_to_n=func_a(n-1)
    answer=sum_to_m-sum_to_n
    return answer

#신수민_12
def func_a(s):
    ret=0
    for i in s:
        if i>ret:
            ret=i

def func_b(s):
    ret=0
    for i in s:
        ret+=i
    return ret

def func_c(s):
    ret=101
    for i in s:
        if i<ret:
            ret=i
    return ret
def solution(scores):
    sum=func_b(scores)
    max_score=func_a(scores)
    min_score=func_c(scores)
    return sum-max_score-min_score
