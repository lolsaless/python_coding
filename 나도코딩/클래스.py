# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력은 {0}, 공격력은 {1}입니다.\n".format(hp, damage))

# # 시즈탱크 : 공격 유닛, 탱크, 일반모드/시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력은 {0}, 공격력은 {1}입니다.\n".format(tank_hp, tank_damage))

# tank_name2 = "탱크"
# tank_hp2 = 150
# tank_damage2 = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name2))
# print("체력은 {0}, 공격력은 {1}입니다.\n".format(tank_hp2, tank_damage2))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank_name2, "1시", tank_damage2)

# # 클래스는 붕어빵 틀이라고 생각하면 된다. 틀에 재료를 넣으면 붕어빵 생성

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력은 {0}, 공격력은 {1}입니다.\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)