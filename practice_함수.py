# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# balance = 10
# balance = deposit(balance, 1000)
# print(balance)

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)


# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원 이며, 잔액은 {1} 원 입니다.".format(commission, balance))



## 기본값
## 역슬러시는 줄 바꿈
# def profile(name, age, main_lang):
#     print("나이 : {0}\t나이 :{1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("나이 : {0}\t나이 :{1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#         print(name, age, main_lang)

# profile(name = "유재석", main_lang = "파이썬", age = 20)

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#         print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
#         print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
            print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
            for lang in language:
                print(lang, end= " ") # 줄바꿈을 하지 않기 위해서 end
            print() # <-- 마지막 print는 줄바꿈을 위해서 넣는다.
            

profile("유재석", 20, "ptyhon", "java", "C", "C++", "C#", "dddd")
profile("김태호", 25, "Kotlin", "Swift")
