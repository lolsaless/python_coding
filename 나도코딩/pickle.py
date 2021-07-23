with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 공부하고 있습니다.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as temp_file:
        temp_file.write("- " + str(i) + "주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :")