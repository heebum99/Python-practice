# 자료형

# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
# '',""(따옴표,쌍따옴표 모두 사용가능)
# 문자열과 정수를 섞어서 사용가능
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# 참/거짓을 표현하는 자료형 boolean
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# 문자열 변수는 ""로 초기화
# 숫자 자료형, boolean형 변수는 print문으로 출력시 str()로 감싸줘야함.
# str() 없이 사용하기 위해서 +가 아닌 ,로 구분 ,가 들어갈 시 공백이 포함됨.
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+animal+"의 이름은 "+name+"예요")
hobby = "공놀이"
print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))

# 주석
# 한줄 주석 처리시 # 사용
# 여러줄 주석 처리시 ' 3개(''')를 사용하거나 ctrl+/를 이용해 여러줄 주석 처리
