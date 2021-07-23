cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet[3])

print(cabinet.get(3))
# print(cabinet[5])
print("hi")
# dict에 키 값이 없으면 오류가 나고 종료됨
print(cabinet.get(5))
print(cabinet.get(5, "사용가능f"))
print("hello")
# get()함수를 사용하면 키값이 없다고 오류가 아닌 None값 실행 후, 다음 코드 실행

print(3 in cabinet)


cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

# 가버린 손님
del cabinet["A-3"]
print(cabinet)

# key 값만 출력
print(cabinet.keys())

# value 값만 출력
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)