# 문자열
sentence = "나는 소년입니다"
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)

# 여러 문장을 포함하는 문자열
# """"(쌍따옴표 3개)를 사용해 그 안에 포함되는 모든 문장이 변수에 저장
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
# 필요한 정보만 잘라서 가져오는것
# []대괄호 안의 값을 가져옴
# x~y 인덱스 범위 값을 가져오려면 [x:y+1]
jumin = "990120-1234567"
print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])  # 0~1 인덱스 범위의 값을 가져옴
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])
print("생년월일 : "+jumin[:6])  # 처음부터 6번째 인덱스전까지 0:6과 동일
print("뒤 7자리 : "+jumin[7:])  # 7번째 인덱스부터 마지막 인덱스까지 7:14와 동일
print("뒤 7자리 (뒤에서부터) : "+jumin[-7:-1])
# 맨 뒤 인덱스를 -1로 생각하고 왼쪽으로 갈수록 -1씩 증가, [-7:]과 동일

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())  # 문자열 모두를 소문자로 변환
print(python.upper())  # 문자열 모두를 대문자로 변환
print(python[0].isupper())  # 대문자 여부 확인
print(len(python))  # 문자열의 길이 반환
print(python.replace("Python", "Java"))  # 해당 문자열을 찾고 다른 문자열로 변환

index = python.index("n")  # 문자열에서 해당 문자가 몇번째 인덱스에 있는지 반환
print(index)
index = python.index("n", index+1)
# index("문자",시작위치), 시작위치 이후의 해당 문자를 찾고 인덱스 반환
print(index)

print(python.find("n"))
# index() 함수와 동일한 기능
# 차이점: index()는 존재하지 않는 문자를 입력시 오류발생, find()는 -1을 반환

print(python.count("n"))  # 문자열 안에 해당 문자 개수 반환

# 문자열 포맷
print("a"+"b")
print("a", "b")

# 방법1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % 'A')
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# 중괄호{} 안에 인덱스 번호를 입력 가능
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법3
# format()에 변수처럼 사용해 {}안에 사용가능
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법4
# 실제 변수의 값을 사용, print(f)로 시작, f는 실제 변수를 가져와 사용한다는 의미
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
# \n: 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# \", \': ",'출력
print("저는 \"나도코딩\"입니다.")

# \\ : \출력
print("\\c\\파이썬\\WorkSpace")

# /r: 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b: 백스페이스
print("Redd\bApple")

# \t: 탭
print("Red\tApple")
