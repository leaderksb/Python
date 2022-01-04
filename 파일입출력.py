score_file = open("score.txt", "w", encoding="utf8")  # 쓰기
print("수학 : 80", file=score_file)
print("영어 : 0", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")  # 추가
score_file.write("과학 : 60")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # 읽기
print(score_file.read())
print()
score_file.close()

print("-----")

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 한줄 읽고 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

print("-----")

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")  # 줄바꿈 없애기
score_file.close()

print("\n-----")

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태
for line in lines:
    print(line, end="")
score_file.close()