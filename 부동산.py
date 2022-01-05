# 지역, 주거 형태, 계약 종류, 가격, 완공년
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# 1) 클래스 생성자에 매개변수 값 저장
# 2) 클래스 내 함수 호출
# House("강남","아파트", "매매", "10억", "2010년").show_detail()
# House("마포","오피스텔", "전세", "5억", "2007년").show_detail()
# House("송파","빌라", "월세", "500/50", "2000년").show_detail()

# 리스트를 사용함
house = []
house1 = House("강남","아파트", "매매", "10억", "2010년")
house2 = House("마포","오피스텔", "전세", "5억", "2007년")
house3 = House("송파","빌라", "월세", "500/50", "2000년")

house.append(house1)
house.append(house2)
house.append(house3)

for h in house:
    h.show_detail()

print("[ 총 " + str(len(house)) + "개의 매물이 있습니다. ]")