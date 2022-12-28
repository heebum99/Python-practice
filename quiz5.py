'''
Quiz)당신의 학교에서는 파이썬 코딩대회를 주최합니다.
참석률을 높이기 위해서 댓글 이벤트를 진행합니다
댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받습니다.
추첨 프로그램을 작성하시오.

조건1: 편의상 댓글은 20명이 작성했고 아이디는 1~20이라 가정
조건2: 댓글내용과 상관없이 무작위로 추첨하되 중복불가
조건3: random 모듈의 shuffle과 sample을 활용

(출력예제)
-- 당첨자 발표 --
치킨 당첨자: 1
커피 당첨자: [2, 3, 4]
-- 축하합니다 --
'''
# from random import *
# lst = [1, 2, 3, 4, 5]
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))  # 리스트 요소 중에서 샘플을 무작위로 인자수 만큼 뽑는다.

from random import *
users = range(1, 21)  # 1부터 20까지 숫자를 생성
# print(type(users))  # 현재 타입은 range
users = list(users)  # list 타입의 함수를 사용해주기 위해 list로 타입 변경
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")
