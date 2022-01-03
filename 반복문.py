for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호: {0}".format(waiting_no))

for waiting_no in range(1, 6):
    print("대기번호: {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 학생 명수를 출석번호로 만들기
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 이름을 길이로 변환
students = ["츠엘", "페리", "플러스"]
students = [len(i) for i in students]
print(students)

# 이름을 대문자로 변환
students = ["Kimsubin", "Kimeunseon", "Kimchanho"]
students = [i.upper() for i in students]
print(students)

# 역에서 5~15분 사이 대기시간의 승객 탑승 시키기
from random import *
cnt = 0  # 총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 :", cnt)