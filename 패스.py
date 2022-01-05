# 일반 유닛
class Unit:
    def __init__(self, name, hp):  # 생성자
        self.name = name
        self.hp = hp

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass  # 아무것도 안하고 그냥 넘김

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()