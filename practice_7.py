# 함수
# 함수정의
def open_account():
    print("새로운 계좌가 생성되었습니다.")


# 함수호출
open_account()


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money  # 리턴


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금(수수료)
    commission = 100  # 수수료 100원
    return commission, balance - money - commission  # 여러개 반환하는 경우 (,)로 구분


balance = 0  # 잔액
balance = deposit(balance, 1000)  # 리턴 값을 balance로 받아줌
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
# 리턴 값이 여러개이므로 리턴된 개수만큼 변수를 통해 받아줌
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 줄바꿈을 할땐 \엔터를 한다.
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
          .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


# 함수 기본값 설정 => 값을 전달받지 않아도 기본 설정값이 전달됨
def profile1(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
          .format(name, age, main_lang))


profile1("유재석")
profile1("김태호")


# 키워드 값 사용,키워드를 사용하면 매개변수 전달시 순서대로 전달하지 않아도 됨
def profile2(name, age, main_lang):
    print(name, age, main_lang)


profile2(name="유재석", main_lang="파이썬", age=20)
profile2(main_lang="자바", age=25, name="김태호")


# 가변인자 => *변수명을 통해 입력받고 for문을 통해서 가변인자에 대해 입력받을 수 있음
def profile3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # end=" "의 의미는 문장이 끝날때 줄바꿈 대신 공백 한칸으로 대체
    # 자바에서 print와 println의 차이
    for lang in language:
        print(lang, end=" ")
    print()


# 가변인자 선언했기에 인자의 개수가 달라도 상관x
profile3("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile3("김태호", 25, "Kotlin", "Swift")


# 지역변수, 전역변수
# 전역변수로 사용하려면 global 변수를 통해서 사용
gun = 10


# 전역변수 사용 예제1
def checkpoint(soldiers):
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    # 원래는 함수 내에 있는 지역변수 gun이지만 global gun을 통해 전역변수 gun을 사용
    print("[함수 내] 남은 총 : {0}".format(gun))


# 전역변수 사용예제2
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
