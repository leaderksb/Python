# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  # 생성자
        self.name = name
        self.hp = hp
        self.speed = speed

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)  # self 없이 사용
        self.location = location

class Unit:
    def __init__(self):  # 생성자
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()  # 맨 처음 클래스만 상속받음
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()