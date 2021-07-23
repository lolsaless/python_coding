subway = ['유재석', '조세호', '박명수']
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명 씩 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람 몇명인지 확인하기
subway.append("유재석")
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두지우기
# num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# list확장
num_list.extend(mix_list)
print(num_list)