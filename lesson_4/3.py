# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

x = 3
y = 3


def pov(a, n):
    if (n == 1):
        return a
    else:
        return a * pow(x, n - 1)


print(pov(x, y))