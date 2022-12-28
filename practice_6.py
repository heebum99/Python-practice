# 분기
weather = input("오늘 날씨는 어때요? ")  # input()안의 문장을 실행후 입력을 받는다.
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))  # 입력받은 데이터를 int형으로 변환
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp:  # and temp < 10은 생략가능
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# 반복문
# for 반복문
for wating_no in [0, 1, 2, 3, 4]:
    # range(5)로 해도 동일
    # range (1,6)으로 하면 1~5번까지
    print("대기번호 : {0}".format(wating_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while 반복문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:  # 무한 루프 => 종료하려면 ctrl + c
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# continue, break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한줄 for문
students = [1, 2, 3, 4, 5]
print(students)
# 1,2,3,4,5 앞에 100을 붙이기로 했다면
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
