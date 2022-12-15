# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
import random
n = int(input('scolko monet? --- '))


def CreateList(a):
    i = 0
    list = []
    while (i < a):
        list.append(random.randint(0, 1))
        i += 1
    return list


money = CreateList(n)
print(money)

if money.count(0) > money.count(1):
    print(f"min kolichestvo = {money.count(1)}")
else:
    print(f"min kolichestvo = {money.count(0)}")
