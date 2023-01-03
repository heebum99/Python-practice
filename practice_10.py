# 예외처리
# try문 안에 에러가 발생했을때 except문 안에 해당 오류가 있으면 그 문장을 실행

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print(str(num1)+"/"+str(num2)+"="+str(int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:  # 정확한 에러내용 표시
    print(err)
except:  # ValueError, zeroDivisionError 외 다른 에러가 발생시 실행
    print("알 수 없는 에러가 발생했습니다.")


# 에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:  # 두 숫자중 하나라도 한자리 숫자가 아니면 ValueError 발생
        raise ValueError  # raise를 통해 특정 에러 발생
    print(str(num1)+"/"+str(num2)+"="+str(int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# 사용자 정의 예외처리


class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:  # 두 숫자중 하나라도 한자리 숫자가 아니면 ValueError 발생
        raise BigNumberError("입력값 : "+str(num1)+", " +
                             str(num2))  # raise를 통해 특정 에러 발생
    print(str(num1)+"/"+str(num2)+"="+str(int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:  # 사용자 정의 예외처리
    print("에러가 발생했습니다. 한자리 숫자만 입력하세요.")
    print(err)
finally:  # finally 문장은 항상 실행됨
    print("계산기를 이용해 주셔서 감사합니다.")
