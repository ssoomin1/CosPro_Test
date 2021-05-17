# def solution(shirt_size):
#     answer=[]
#     answer=[0 for _ in range(6)]
#     for shirt in shirt_size:
#         if shirt == "XS":
#             answer[0]+=1
#         elif shirt=="S":
#             answer[1]+=1
#         elif shirt=="M":
#             answer[2]+=1
#         elif shirt=="L":
#             answer[3]+=1
#         elif shirt=="XL":
#             answer[4]+=1
#         elif shirt=="XXL":
#             answer[5]+=1
#     return answer
#
# shirt_size=["XS","S","XXL","L","L","XL","S"]
# print(solution(shirt_size))

number=234
print(number)
number=number%10 #일의 자리 4가 나머지가 된다.
print("일의자리:",number)
# number=number//10 #나머지 : 3 => 십의 자리
# print(number)
# number=number//10 #나머지: 2 => 백의 자리
# print(number)

