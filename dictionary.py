# 딕셔너리 : Key와 Value를 한 쌍으로 갖는 자료형
# 형식 key : value

cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5])  # 값이 없으면 오류 메세지 출력 후 종료
print(cabinet.get(5))  # 값이 없으면 None 출력 후 나머지 코드 실행
print(cabinet.get(5, "사용가능"))  # 값이 없으면 설정된 기본값을 넣어서 출력

# 해당 키가 딕셔너리에 존재 하는가
print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 값 수정
print(cabinet)
cabinet["A-3"] = "김종국"

# 값 추가
cabinet["C-20"] = "조세호"
print(cabinet)

# 값 삭제
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