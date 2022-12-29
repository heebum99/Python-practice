# 표준입출력

# 표준출력
# +가 아닌 ,로 구분시 기본값은 공백한칸, sep을 통해 구분문자 지정가능
# end를 통해 문장의 끝부분을 처리하는 문자 지정가능
import pickle
import sys
print("Python", "Java", "JavaScript", sep=",", end="?")  # 구분문자는 (,) 문장 끝은 (?)
print("무엇이 더 재밌을까요?")

print("Python", "Java", file=sys.stdout)  # 표준 출력으로 문장이 처리
print("Python", "Java", file=sys.stderr)  # 표준 에러로 문장이 처리

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
# dictionary에서 items()를 사용하면 key, value값을 쌍으로 받아온다.
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # subject 부분은 8칸을 확보해 왼쪽정렬을, score 부분은 4칸을 확보해 오른쪽 정렬을 한다는 의미

# 은행 대기순번표
# 001,002,003 ...
for num in range(1, 21):
    print("대기번호 : "+str(num).zfill(3))  # 3개의공간으로 구성을 하며 값이 없는 공간에는 0으로 채워넣는다


# 표준 입력
# 사용자 입력 형태로 입력을 받을 경우 항상 문자열로 입력을 받는다(정수를 입력해도 동일)
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 "+answer+"입니다.")


# 다양한 출력 포맷
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽정렬을 하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마(,)를 찍어주기
print("{0:,}".format(1000000000000))

# 3자리마다 콤마를 찍으며 +-부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리마다 콤마를 찍으며, 부호도 붙이고, 자릿수 확보하고 빈자리는 ^로 채우기
print("{0:^<+30,}".format(1000000000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수까지 표시
print("{0:.2f}".format(5/3))  # 소수점 둘째자리까지만 표시, 셋째자리에서 반올림


# 파일 입출력
# score.txt파일에 (w)쓰기위한 목적으로 열고 encoding은 utf8로 하겠다.
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# w는 내용이 있으면 덮어씌우는것 a는 이어서 쓰는것
# write()로 쓰면 줄바꿈이 따로 적용이 안되므로 개행문자 필요
score_file1 = open("score1.txt", "a", encoding="utf8")
score_file1.write("과학: 80")
score_file1.write("\n코딩 : 100")
score_file1.close()

# r은 읽어오는 용도로 파일을 열겠다
score_file2 = open("score1.txt", "r", encoding="utf8")
print(score_file2.read())  # read()를 통해 모든 내용을 다 불러오는것
score_file2.close()

score_file3 = open("score1.txt", "r", encoding="utf8")
while True:
    line = score_file3.readline()  # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
    if not line:  # 읽어올 내용이 없으면 break
        break
    print(line, end="")
score_file3.close()

# list 형태로 읽어오는 방법
score_file4 = open("score.txt", "r", encoding="utf8")
lines = score_file4.readlines()  # list형태로 저장
for line in lines:
    print(line, end="")
score_file4.close()


# pickle => 프로그램상에서 사용하고 있는 데이터를 파일형태로 저장하고 사용하는 것
# pickle 파일 저장
profile_file = open("profile.pickle", "wb")  # pickle을 쓰기 위해서 항상 바이너리(b)파일로 설정
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()


# pickle 파일 읽어오기
profile1_file = open("profile.pickle", "rb")
profile1 = pickle.load(profile1_file)  # file에 있는 정보를 profile1에 불러오기
print(profile1)
profile1_file.close()


# with 활용
with open("profile.pickle", "rb") as profile2_file:
    # file을 열어서 profile2_file 변수에 저장하고 파일 내용을 load()를 통해 불러온다
    print(pickle.load(profile2_file))
    # close() 필요 없이 with문이 종료시 종료됨

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study1_file:
    print(study1_file.read())
