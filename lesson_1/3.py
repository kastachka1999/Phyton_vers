# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
#  за проезд и получали билет с номером. Счастливым билетом называют такой билет
#  с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
#  которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

import random
a = list(str(int(random.random()*1000000)))
print(a)


def Ves(x, y):
    if x == y:
        return print("о счастливчик(yes)")
    else:
        return print("повезет в следующий раз (no)")


def Happinies(x):
    i = 0
    j = len(a) - 1
    sum1 = 0
    sum2 = 0
    while (i <= len(a)/2 - 1):
        sum1 += int(a[i])
        i += 1
        sum2 += int(a[j])
        j -= 1
    return Ves(sum1, sum2)


Happinies(a)
