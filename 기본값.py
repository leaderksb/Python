def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))

profile("김수빈", 21, "파이썬")
profile("김은선", 50, "자바")

# 기본값 설정
def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))

profile("김대학")