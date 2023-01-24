# Вычислить значение выражения

# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15

str = '12 * 15'

lis = str.split()


def Two(mas):
    a = int(mas[0])
    b = mas[1]
    c = int(mas[2])
    if b == '+':
        return a + c
    if b == '-':
        return a - c
    if b == '/':
        return a / c
    if b == '*':
        return a * c
