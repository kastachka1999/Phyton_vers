# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


a = list(str(input("vvedite chislo :")))

if len(a) == 3:

    def sum(x):
        sum = 0
        for i in a:
            sum = sum + int(i)
        return sum
    print(f'summa = {sum(a)}')
else:
    print("vvesite trehznachnoe")
