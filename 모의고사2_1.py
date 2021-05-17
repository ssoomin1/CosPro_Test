#신수민
def solution(n,price):
    games=n*(n-1)//2 #총 게임수
    per_day=n//2 #하루에 할 수 있는 경기 수(하루에 한 경기만)
    answer=(games//per_day)*price #대회기간
    return answer
teams=8
price=100000
ret1=solution(teams,price)
print(ret1)

