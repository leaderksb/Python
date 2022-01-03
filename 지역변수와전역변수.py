gun = 10  # 전역변수

def checkpoint(soldiers):  # 경계근무
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers  # 지역변수
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun  # 지역변수 리턴

print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)  # 지역변수를 전역변수에 저장
print("남은 총 : {0}".format(gun))