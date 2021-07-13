# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}

for subjects, score in scores.items():
    print(subjects.ljust(3), str(score).rjust(4), sep=":")
    

