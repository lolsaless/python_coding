cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet[3])

print(cabinet.get(3))
# print(cabinet[5])
print("hi")
# dict에 키 값이 없으면 오류가 나고 종료됨
print(cabinet.get(5))
print("hello")
# get()함수를 사용하면 키값이 없다고 오류가 아닌 None값 실행 후, 다음 코드 실행
