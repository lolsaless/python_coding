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


print('a' + 'b')

print("나는 %d살입니다." %20)
print("나는 %s을 좋아해요" %'파이썬')

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format('파란', '빨간'))
print("나는 {1}색과 {0}색을 좋아합니다.".format('파란', '빨간'))


print('나는 {age}살이며, {color}색을 좋아합니다.'.format(age=20, color="빨강"))

age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아합니다 ")

#\n 줄바꿈
print("백문이 불여일견,\n백견이 불여일타")

print('저는 "나도코딩" 입니다.')

print("저는 \"나도코딩\"입니다.")

#\\ : 문장 내에서는 \로 나타남

#\r : 커서를 맨 앞으로 이동
print("red white apple\rPine")

#\b : 백스페이스(한 글자 삭제)
print("redd\bApple")

#\t : tab
print('red\tapple\nwhite')


#Quiz
http = "http://naver.com"
http = "http://daum.net"
http_split = http.split('//')
print(http_split[1])
http_naver = http_split[1]
http_naver_split = http_naver.split('.')
naver = http_naver_split[0]
print(naver)

password = naver[:3] + str(len(naver)) + str(naver.count('e')) + "!"
print(password)

my_str = http.replace('http://', '')
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(http, password))



my_str = http.replace('http://', '')
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print(f"{http}의 비밀번호는 {password}입니다.")