# 모듈 사용하기
# 모듈은 사용하려면 파일과 같은 경로나 라이브러리가 모여있는 폴더에 있어야 사용가능

import datetime
import time
import os
import glob
from bs4 import BeautifulSoup
import random
import inspect
from travel import *
from travel import vietnam
from travel.thailand import ThailandPackage
import travel.thailand  # 패키지 활용
# theater_module의 price와 price_morning 함수만 사용가능
from theater_module import price, price_morning
from theater_module import *  # theater_module 이나 mv처럼 따로 호출할 필요없이 모듈 내용 사용가능
import theater_module as mv  # theater_module 대신 mv로 호출가능
import theater_module
theater_module.price(3)  # 3명이 영화보러 갔을때 가격
theater_module.price_morning(4)  # 4명이 조조할인 영화보러 갔을때 가격
theater_module.price_soldier(5)  # 5명의 군인이 영화보러 갔을때 가격

# import theater_module as mv 덕분에 아래와 같이 사용가능
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# from theater_module import * 덕분에 아래와 같이 사용가능
price(3)
price_morning(4)
price_soldier(5)

# import travel.thailand => 모듈이나 패키지만 가능, 클래스나 함수는 import 불가
trip_to = travel.thailand.ThailandPackage()  # ThailandPackage 객체 생성
trip_to.detail()

# from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

# from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# from travel import * => 이렇게 사용하려면 개발자가 공개범위를 설정을 해줘야한다.
# __init__ 모듈을 통해서 공개 범위를 설정해준다.
trip_to = thailand.ThailandPackage()
trip_to.detail()

# import inspect => 모듈, 패키지의 위치를 알려주는 메소드 포함
# import random
print(inspect.getfile(random))  # random 모듈이 어느 위치에 있는지 알려줌
print(inspect.getfile(thailand))

# pip install => pypi에서 검색
# beautiful soup4 => 웹페이지의 정보를 쉽게 스크랩할 수 있게 해줌
# from bs4 import BeautifulSoup
# 터미널에서 pip list를 통해 설치되어있는 pip 확인가능
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 내장함수

# input: 사용자 입력을 받는 함수
languague = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(languague))

# dir: 어떤 객체를 넘겨줬을때 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
print(dir(random))
lst = [1, 2, 3]
print(dir(lst))
name = "Jim"
print(dir(name))

# 외장함수

# glob: 경로내의 폴더/파일 목록 조회(윈도우 dir)
# import glob
print(glob.glob("*.py"))  # .py로 끝나는 모든 파일에 대한 결과를 표시

# os: 운영체제에서 제공하는 기본기능
# import os
print(os.getcwd())  # 현재 디렉토리 표시
folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제했습니다.")
else:
    os.makedirs(folder)  # 폴더생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())

# time: 시간관련 함수
# import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# datetime
# import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta: 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은", today+td)  # 오늘부터 100일 후
