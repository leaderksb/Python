sentence1 = '나는 토끼입니다'
print(sentence1)

sentence2 = "파이썬을 공부해봅시다"
print(sentence2)

sentence3 = """
나는 토끼이고,
파이썬을 공부해봅시다
"""
print(sentence3)

print("a" + "b")
print("a", "b")

# %s
print("저는 %s을 좋아해요." % "파이썬")
print("저는 %s색과 %s색을 좋아해요." % ("흰", "검은"))

# 방법 1
print("저는 %d살입니다." % 20)
print("Python은 %c로 시작해요." % "P")

# 방법 2
print("저는 {}살입니다.".format(20))
print("저는 {}와 {}을 좋아해요.".format("토끼", "사슴"))
print("저는 {0}와 {1}을 좋아해요.".format("토끼", "사슴"))
print("저는 {1}와 {0}을 좋아해요.".format("토끼", "사슴"))

# 방법 3
print("저는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "주황"))
print("저는 {age}살이며, {color}색을 좋아해요.".format(color = "주황", age = 20))

# 방법 4 (v3.6 이상)
age = 20
color = "초록"
print(f"저는 {age}살이며, {color}색을 좋아해요.")
