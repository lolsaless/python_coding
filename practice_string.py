sentence = '나는 소년입니다.'
sentence2 = "파이썬은 쉽습니다."
sentence3 = """
나는 소년이고,
파이썬은 쉽습니다.
"""

print(sentence3)


#데이터 슬라이싱
number = "860101-1143419"
print("성별:" + number[7])
print(number.split('-')[0][1])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(not(python[0].isupper()))
print(len(python))

print(python.replace("Python", "Java"))

index = python.index("n")

print(index)

index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("n",6))

print(python.count("n"))