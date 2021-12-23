n = None
print(n)
# 리스트 : 비슷한 성질을 가진 객체의 나열
# 인덱스 :  0   1   2   3
#    값 : 3.5 4.3 2.3 3.8
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

# 정렬
num = [5, 2, 4, 3, 1]
num.sort()
print(num)

# 순서 뒤집기
num.reverse()
print(num)

# 모두 지우기
# num.clear()
# print(num)

# 다양한 자료형과 함께 사용
mix = ["김수빈", 20, True]
print(mix)

# 확장
mix.extend(num)
print(mix)

subway = ["김수빈", "토미", "츠엘"]
print(subway)

# 김수빈이 몇번째 칸에 타고 있는가?
print(subway.index("김수빈"))

# 플러스가 다음 정류장에서 다음 칸에 탐
subway.append("플러스")
print(subway)

# 페리를 츠앨과 플러스 사이에 태움
subway.insert(3, "페리")
print(subway)

# 지하철 탑승객을 하나씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
print(subway.count("김수빈"))