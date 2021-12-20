from math import *
from random import *

# 숫자처리함수
print(abs(-5))  # 절대값
print(pow(4, 2))  # 밑과 지수 제곱
print(max(5, 12))  # 최대값
print(min(5, 12))  # 최소값
print(round(3.14))  # 반올림
print(floor(4.99))  # 내림
print(ceil(3.14))  # 올림
print(sqrt(16))  # 제곱근

# 랜덤함수
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(randrange(1, 50))  # 1 ~ 50 미만의 임의의 값 생성
print(randint(1, 50))  # 1 ~ 50 미만의 임의의 값 생성
