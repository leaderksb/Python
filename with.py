import pickle

# profile.pickle을 읽어서 profile_file에 저장
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))  # 클로즈 할 필요 없음

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())