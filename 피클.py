# 피클 : 가지고 있는 데이터를 파일에 저장한 후, 불러와서 사용할 수 있게 도와줌
import pickle

profile_file = open("profile.pickle", "wb")  # 바이너리 타입 쓰기
profile = {"이름":"김수빈", "나이":21, "취미":["노래", "녹음", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")  # 바이너리 타입 읽기
profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()