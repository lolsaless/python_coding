for waiting_no in range(0,5):
    print("대기번호 {0}".format(waiting_no))

starbucks = ["iron man", "Thor", "Hulk"]
for customer in starbucks:
    print("{}, 커피가 준비되었습니다.".format(customer))


# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

student = range(1,6)
student = [i+100 for i in student]
print(student)

# 학색 이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [len(i) for i in student]
print(student)

student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student]
print(student)