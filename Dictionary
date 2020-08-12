cabinet = {3:"유재석", 100:"김태호"}
# 딕셔너리란 Key와 Value를 한 쌍으로 갖는 자료형
# 형식 key:value

print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# print(cabinet[5])
# 값이 없으면 오류 메세지 출력 후 종료
print(cabinet.get(5))
# 값이 없으면 None 출력 후 나머지 코드 실행
print(cabinet.get(5, "사용가능"))
# 값이 없으면 값을 넣어서 출력

print(3 in cabinet) # True
print(5 in cabinet) # Flase
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 값 추가, 수정, 삭제
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# key, value 삭제
cabinet.clear()
print(cabinet)
