# 리스트[] => 배열
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))
subway.append("하하")
print(subway)

# 인덱스 번호 위치에 요소 추가
subway.insert(1, "정형돈")
print(subway)

# 맨 마지막요소부터 꺼냄(삭제).
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 리스트 요소 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)

# 사전 {key:value}
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])  # get()과 동일
print(cabinet[100])  # key값이 존재하지 않으면 오류발생
print(cabinet.get(3))  # key값이 존재하지 않으면 None 출력
print(cabinet.get(5, "사용 가능"))  # key 값 5가 존재하지않으면 사용가능 출력

# key 값 보유 여부 확인
print(3 in cabinet)  # key 값 3이 있으면 True 없으면 False 출력
print(5 in cabinet)

# key 값은 문자열도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet)

# 새로운 요소 추가
cabinet["C-20"] = "조세호"
print(cabinet)
cabinet["A-3"] = "김종국"
print(cabinet)

# 기존 요소 삭제
del cabinet["A-3"]
print(cabinet)

# key 값만 출력
print(cabinet.keys())

# value 값만 출력
print(cabinet.values())

# key,values 쌍으로 출력
print(cabinet.items())

# 모든 요소 삭제
cabinet.clear()
print(cabinet)

# 튜플
# 내용 변경, 추가x
menu = ("돈까스", "치즈까스")
print(menu)
print(menu[0])
print(menu[1])

(name, age, hobby) = ("김종국", 20, "코딩")  # 아래와 동일
# name = "김종국"
# age = 20
# hobby = "코딩"
print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 구하기
print(java & python)
print(java.intersection(python))

# 합집합 구하기
print(java | python)
print(java.union(python))

# 차집합 구하기
print(java-python)
print(java.difference(python))

# 집합에 요소 추가
python.add("김태호")
print(python)

# 집합에 요소 삭제
java.remove("김태호")
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))  # 현재 자료형은 set

menu = list(menu)
print(menu, type(menu))  # 현재 자료형은 list

menu = tuple(menu)
print(menu, type(menu))  # 현재 자료형은 tuple

menu = set(menu)
print(menu, type(menu))  # 현재 자료형은 set
