#2209 신수민
a=input("영문자 입력>>")
print(a[0].upper()+a[1:])

date=input("날짜(년/월/일:4자리/2자리/2자리) 입력>> ")
year=date[0:4]
month=date[5:7]
day=date[8:]
print("입력한 날짜의 10년 후>> ",int(year)+10,"년",month,"월",day,"일")