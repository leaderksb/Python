jumin = "021228-4876543"

if jumin[7] == "1" or jumin[7] == "3":
    print("성별 : 남성")
if jumin[7] == "2" or jumin[7] == "4":
    print("성별 : 여성")

print("연 : " + jumin[0:2])  # 0 ~ 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])  # 처음 ~ 6 직전까지
print("뒤 7자리 : " + jumin[7:])  # 7 ~ 끝까지
print("뒤 7자리 (뒤부터) : " + jumin[-7:])  # 맨 뒤 7번째부터 끝까지
