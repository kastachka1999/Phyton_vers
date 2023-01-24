# Уровень 2:
# Количество действий произвольное
#12 + 15 - 4

str = '11 + 1 - 2 + 3 + 2 - 2 + 1 - 2'  # 12

lin = str.split()

print(lin)


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


print(Long(lin))
