# Уровень 3:
# Действия имеют приоритет
#12 - 4*2 +6/3

str = '12 - 4 * 2 + 6 / 3'  # 6

first = str.split()


def Long(mas):
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


def CreateMas(mas):  # преобразование из произведения (part 2)
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


print(CreateMas(first))
print(Long(CreateMas(first)))
