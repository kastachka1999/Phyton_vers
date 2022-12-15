# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import math
N = int(input("vvedite chislo: "))
n = int(math.log(N, 10)/math.log(2, 10))


pr = 1
i = 1
print(f"2 ** {0} == {1}")
while (i <= n):
    pr *= 2
    print(f"2 ** {i} == {pr}")
    i += 1

# если самому описывать принцип функции math.log


def Log(ch, base):
    i = 0
    pro = 1
    while (pro < ch):
        pro *= base
        i += 1
    return i - 1


print(Log(N, 2))
