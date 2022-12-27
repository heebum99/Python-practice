
from random import *
from math import *
# 연산자

print(1+1)  # 2
print(3-2)  # 1
print(5*2)  # 10
print(6/3)  # 2

print(2**3)  # 2^3 = 8
print(5 % 3)  # 나머지 구하기 2
print(10 % 3)  # 1
print(5//3)  # 몫 구하기 1
print(10//3)  # 3

print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True

# !과 not은 부정
print(3 == 3)  # True
print(4 == 2)  # False
print(3+4 == 7)  # True
print(1 != 3)  # True
print(not (1 != 3))  # False

# and와 &는 같은 의미로 모두 만족시킬때 True 반환
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

# or과 |는 같은 의미로 둘 중 하나라도 만족시키면 True 반환
print((3 > 0) or (3 > 5))  # True
print((3 > 0) | (3 > 5))  # True

print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False


# 수식
print(2+3*4)  # 14
print((2+3)*4)  # 20
number = 2+3*4  # 14
print(number)
number = number+2  # 16
print(number)
number += 2  # number = number + 2와 같은 의미
print(number)  # 18
number *= 2  # 36
print(number)
number /= 2  # 18
print(number)
number -= 2  # 16
print(number)
number %= 5  # 1
print(number)

# 숫자처리 함수
print(abs(-5))  # 절댓값 출력
print(pow(4, 2))  # 거듭제곱값 출력
print(max(5, 12))  # 최대값 출력
print(min(5, 12))  # 최소값 출력
print(round(3.14))  # 반올림
print(round(4.99))

# math 라이브러리 활용
# from math import *
print(floor(4.99))  # 내림
print(ceil(3.14))  # 올림
print(sqrt(16))  # 제곱근

# random 함수(난수) 활용
# from random import *
print(random())  # 0.0이상 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0~10.0 미만의 임의의(실수) 값 생성
print(int(random() * 10))  # 0~10 미만의 정수값 생성
print((int(random() * 10)) + 1)  # 1~10 이하의 정수값 생성

print((int(random() * 45) + 1))  # 1~45 이하의 임의의 값 생성
print(randrange(1, 46))  # 1~46 미만의 임의의 값 생성
print(randint(1, 45))  # 1~45 이하의 임의의 값 생성
# 3개의 문장이 모두 동일
