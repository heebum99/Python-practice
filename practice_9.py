# 클래스
# __init__이란? => 생성자, 객체가 생성될때 자동으로 호출되는 것
# 객체 생성시 __init__의 인자 개수만큼 보내줘야함
class Unit:
    def __init__(self, name, hp, damage):
        # self.name, self.hp, self.damage는 멤버변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
# 멤버 변수를 클래스 밖에서 호출하기 위해 객체.멤버변수로 호출
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
wraith2 = Unit("빼앗은 레이스", 80, 5)
# 클래스 밖에서 멤버변수를 생성해서 사용할 수 있음
wraith2.clocking = True


if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


class AttackUnit:
    def __init__(self, name, hp, damage):
        # self.name, self.hp, self.damage는 멤버변수
        self.name = name
        self.hp = hp
        self.damage = damage

    # 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


# 상속
# Unit2와 AttackUnit2의 공통된 부분이 많으므로 상속을 이용

# 부모 클래스
class Unit2:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# 자식클래스
class AttackUnit2(Unit2):
    def __init__(self, name, hp, damage):
        # 상속하는 Unit클래스의 생성자를 호출
        Unit2.__init__(self, name, hp)
        self.damage = damage

    # 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat2 = AttackUnit2("파이어뱃", 50, 16)
firebat2.attack("5시")
firebat2.damaged(25)
firebat2.damaged(25)


# 다중상속
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))


# 다중상속 시 ,로 구분
class FlyableAttackUnit(AttackUnit2, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit2.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


# 메소드 오버로딩
class Unit3:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도: {2}]"
              .format(self.name, location, self.speed))


class AttackUnit2(Unit3):
    def __init__(self, name, hp, damage, speed):
        # 상속하는 Unit클래스의 생성자를 호출
        Unit3.__init__(self, name, hp, speed)
        self.damage = damage

    # 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable2:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))


class FlyableAttackUnit2(AttackUnit2, Flyable2):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit2.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    # move() 메소드 재정의(오버로딩)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = AttackUnit2("벌쳐", 80, 20, 10)
vulture.move("11시")
battlecruiser = FlyableAttackUnit2("배틀크루저", 500, 25, 3)
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")


# pass
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass  # 오류가 발생하지않고 일단 넘어감. 완성된것 같은 효과를 줌.


game_start()
game_over()


# super
class BuildingUnit(Unit3):
    def __init__(self, name, hp, location):
        # Unit3.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)  # 위의 내용과 동일하지만 super는 ()가 필요하고 self가 필요없음
        self.location = location


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


class Unit4:
    def __init__(self):
        print("Unit 생성자")


class Flyable3:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit4, Flyable3):
    def __init__(self):
        # super().__init__()   이 경우 Unit4의 생성자만 호출됨
        # 모든 생성자의 호출이 필요한 경우
        Unit4.__init__(self)
        Flyable3.__init__(self)


dropship = FlyableUnit()
