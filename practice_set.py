# 집합(set)
# 중복될 수 없음, 순서 없음

my_set = {1,2,3,3,3,3,3}
print(my_set)

# set 정의 하는 방법
java = {"you", "kim", "yang"}
python = set(["you", "park"])

# 교집합 java 와 python을 모두 할 수 있는
print(java & python)
print(java.intersection(python))

# 합집합 java를 할 수 있거나 python을 할 수 있는
print(java | python)
print(java.union(python))

# 차집합 java를 할 수 있지만, python을 할 수 없는
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("kim")
print(python)

# java를 잊었을 때
python.remove("kim")
print(python)