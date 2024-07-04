hello_world = "엄마가 말했다. '밥 먹었니'?"
print(hello_world)
money = 100
name =  "김민석"
print("안녕하세요. " + name + "님 반갑습니다.")
print("입력하신 금액은", money, "원 입니다.")

#  데이터 출력시 , % 기호 사용법

print("저의 이름은 %s 입니다." %name)

number = 10000
print("입력하신 금액은 %d원 입니다."%number)
a = 7
b = 3
result = a + b
print(result)

# 문자열 길이 구하기
hello_world = "엄마가 말했다. '밥 먹었니'?"
print(len(hello_world))

# 인덱싱 슬라이싱
자유로운_문자열 = "엄마가 말했다. '밥 먹었니'?"
print(len(자유로운_문자열))
print(자유로운_문자열[0:7])

# 문자열 치환
data = "2010.08.16"
print("바꾸기 전 데이터:", data)
data = data.replace(".","_")
print("바꾼 후 데이터:", data)

# 연습문제
b = "abcd"
b = b.replace("a","A")
print("바꾼 후 데이터:", b)

# 문자열 거꾸로
a = "Python"
new = a[5]+a[4]+a[3]+a[2]+a[1]+a[0]
print(new)

# 문자열 여러 줄 출력하기
문자열 = "엄마가 말했다. '밥 먹었니'?\n저는 학교를 갑니다."
print(문자열)

