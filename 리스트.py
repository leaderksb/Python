# -*- coding: utf-8 -*-
n = None
print(n)
# 리스트: 비슷한 성질을 가진 객체의 나열
# 인덱스:  0   1   2   3
#     값: 3.5 4.3 2.3 3.8
a = [3.5, 4.3, 2.3, 3.8]
print("인덱스 0 = ", a[0])
print("인덱스 1 = ", a[1])
print("인덱스 2 = ", a[2])
print("인덱스 3 = ", a[3])
sum = 0
for i in a:
    sum = sum + i
print("평균 점수: ", sum/len(a))
b = [
    [90, 95, 83, 40, 30, 20, 19, 48, 39, 59],
    [48, 53, 64, 76, 58, 34, 55, 85, 96, 85]
    ]
sumu = 0
english = b[0]
for i in english:
    sumu = sumu + i
print("영어 평균 점수: ", sumu/len(english))
