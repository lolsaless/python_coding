customer = "Thor"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피 판매를 종료합니다.")

customer = "iron man"
index = 1
while True:
    print("{0}, 커피가 {1}준비 되었습니다.".format(customer, index))
    index += 1
    if index == 10:
        print("종료합니다.")
        break

customer = 'Thor'
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")