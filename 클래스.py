# 마린 : 공격 유닛, 군인, 총 사용 가능
marines_name = "마린"  # 유닛의 이름
marines_hp = 40  # 유닛의 체력
marines_damage = 5  # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(marines_name))
print("{0} 체력 : {1}\n{0} 공격력 : {2}".format(marines_name, marines_hp, marines_damage))

# 탵크 : 공격 유닛, 탱크 , 포 사용 가능, 일반 모드 / 시즈 모드
tank_name = "탱크"  # 유닛의 이름
tank_hp = 150  # 유닛의 체력
tank_damage = 35  # 유닛의 공격력

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(marines_name, "1시", marines_damage)
attack(tank_name, "1시", tank_damage)

# 클래스 : 내용물을 만들낼 수 있는 틀 또는 설계도
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다. ".format(self.name))
        print("{0} 체력 : {1}\n{0} 공격력 : {2}".format(self.name, self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
