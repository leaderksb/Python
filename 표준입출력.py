import sys

print("파이썬", "자바", "코틀린", sep=" VS ", end="?\n")
print("무엇이 더 재밌을까요?")

print("파이썬", "자바", "코틀린", file=sys.stdout)  # 표준 출력
print("파이썬", "자바", "코틀린", file=sys.stderr)  # 표준 에러

# 시험 성적
scores = {"수학":80, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기 순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))  # 특정 길이가 되도록 문자열 앞을 0으로 채움

answer = input("아무 값이나 입력하세요 : ")  # 사용자 입력 값은 문자열 타입
print("입력하신 값은 " + answer + "입니다.")