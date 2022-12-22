# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)#
# O#utput: 11 6
# 6 12
#list(random.randint(0, 100) for i in range(3))
import random
n = int(input("введите n: "))
m = int(input("введите m: "))
first = list(random.randint(0, 10) for i in range(n))
second = list(random.randint(0, 10) for i in range(n))


def Result(big, small):
    exit = []
    for el in small:
        if (big.count(el)):
            exit.append(el)
    exit.sort()
    return exit


def Preview(a):
    for el in a:
        return print(el)


print(first)
print(second)

if (len(Result(first, second)) != 0):
    Preview(Result(first, second))
else:
    print('схожих чисел нет')
