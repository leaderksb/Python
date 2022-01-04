import pickle

# profile.pickle을 읽어서 profile_file에 저장
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))  # 클로즈 할 필요 없음

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# 1~50주차까지 기본 포맷이 설정돼 있는 보고서 파일 생성
for i in range(1, 51):
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as q_file:
        q_file.write("- {0}주차 주간보고 -\n".format(i))
        q_file.write("부서 : \n")
        q_file.write("이름 : \n")
        q_file.write("업무 요약 : \n")

for i in range(1, 51):
    with open("{0}주차.txt".format(i), "r", encoding="utf8") as q_file:
        print(q_file.read())
