# Задача 28
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

x = 4
y = 5


def ch(r, z=0):
    if (r == z):
        return z
    else:
        return ch(r, z+1)


def sum(a, b, z=0, c=0):
    if (z == a and c == b):
        return z + c
    else:
        if (c == b):
            return sum(a, b, z + 1, c)
        else:
            return sum(a, b, z, c+1)


def sum2(a, b):
    return ch(a) + ch(b)


print(f"{sum2(x, y)} == {sum(x,y)}")
