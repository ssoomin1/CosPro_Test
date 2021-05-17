#2209 신수민
#순차적인 값을 가질때만 컴프리헨션 사용
print("수학점수 5개를 입력하세요")
scores=[]
for i in range(5):
    score=int(input("입력>>"))
    scores.append(score)
sum=0
for i in scores: #리스트 원소가 있을때까지
     sum+=i
print("평균 = ",sum/len(scores))