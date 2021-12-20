a = "Hello WORLD"
s = a.strip("Hello")
p = a.split(" ")  # 특정 문자를 기준으로 문자열을 나눔
z = a.zfill(20)  # 특정 길이가 되도록 문자열 앞을 0으로 채움
num1 = "9000"
num2 = int(num1)

print(a.count('L'))
print(a.find("WOR"))  # 원하는 문자열 찾기, 없을 시 -1 반환
print(a.lower())  # 소문자
print(a.upper())  # 대문자
print(a[0].isupper())  # 해당 문자가 대문자인가
print(len(a))  # 문자열 길이
print(a.replace("Hello", "Hi"))  # 문자열 교체
print(s)
print(p)
print(z)
print(num2 + 900)
print(a.index("O"))  # 문자열 내 동일한 해당 문자의 인덱스 번호, 없을 시 오류 발생
