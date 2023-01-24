# Уровень 4 * (дополнительная задача, сдавать не обязательно)
# Действия разделяются скобками
# (12 - 4) * 2


str = '1 + ( 12 - 4 + 3 ) * 2 + 1 + ( 2 + 2 )'  # 28
ln = str.split()
# возврат результ int


def Long(mas):  # вычисление длиного произведения (part 3)
    a = int(mas[0])
    b = mas[1]
    c = int(mas[2])
    result = 0

    if b == '+':
        result += a + c
    if b == '-':
        result += a - c

    i = 3

    while (i < len(mas) - 1):
        if mas[i] == '+':
            result += int(mas[i + 1])
        if mas[i] == '-':
            result -= int(mas[i + 1])
        i += 2

    return result

# возврат массива


def CreateMasSum(mas):  # преобразование из произведения (part 2)
    i = 1

    while (i <= len(mas)):
        if mas.count('*') > 0:

            result = int(mas[mas.index('*') - 1]) * \
                int(mas[mas.index('*') + 1])
            mas.pop(mas.index('*') - 1)
            mas.pop(mas.index('*') + 1)
            mas[mas.index('*')] = int(result)
            continue

        if mas.count('/') > 0:
            result = int(mas[mas.index('/') - 1]) / \
                int(mas[mas.index('/') + 1])
            mas.pop(mas.index('/') - 1)
            mas.pop(mas.index('/') + 1)
            mas[mas.index('/')] = int(result)
            continue
        i += 1

    return mas


def CreateMasPrz(mas):
    while (mas.count('(')) > 0:

        lin = []
        a = mas.index('(')
        b = mas.index(')')
        i = a + 1
        while (i < b):
            lin.append(mas[i])
            i += 1
        i = a + 1
        while (a < b):
            mas.pop(i)
            a += 1
        mas[mas.index('(')] = int(Long(lin))

    return mas


print(CreateMasPrz(ln))
print(CreateMasSum(CreateMasPrz(ln)))
print(Long(CreateMasSum(CreateMasPrz(ln))))
