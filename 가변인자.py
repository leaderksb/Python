# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("김수빈", 21, "Python", "Java", "C", "C++", "C#")
# profile("김은선", 50, "Kotlin", "Swift", "", "", "")
profile("김은선", 50, "Kotlin", "Swift")