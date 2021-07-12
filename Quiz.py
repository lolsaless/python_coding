from random import *

count = 0
for customer in range(1, 51):
    time = randint(5,50)

    if 5 <= time and 15 >= time:
        print("[O]{0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        count += 1
    else:
        print("[ ]{0}번째 손님 (소요시간 : {1}분)".format(customer, time))

print("총 탑승 승객 : {}명".format(count))


def std_weight(height, gender):
    heights = height/100
    if gender == "남자":
        man = heights**2 * 22
        man = round(man, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, man))
    elif gender == "여자":
        girl = heights**2 * 21
        girl = round(girl, 2)
        print("키 {0}cm 여쟈의 표준 체중은 {1}kg 입니다.".format(height, girl))


std_weight(175, "남자")