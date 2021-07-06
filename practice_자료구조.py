# menu = {"coffe", "milk", "juice"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


# Quiz
from random import *

users_1round = range(1, 21)
users_1round = list(users_1round)
shuffle(users_1round)

first_chicken = sample(users_1round, 1)

users_2round = list()

for i in users_1round:
    if i != first_chicken[0]:
        users_2round.append(i)

second_coffee = sample(users_2round, 3)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}".format(first_chicken))
print("커피 당첨자 : {}".format(second_coffee))
print(" -- 축하합니다 -- ")