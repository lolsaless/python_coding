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

lst = [1,2,3,4,5]
shuffle(lst)
lists = list()
for i in lst:
    lists.append(i)

print(lists)

a = sample(lists, 3)
print(a)

