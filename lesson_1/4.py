# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

len = 3
wid = 2
k = 1
l = 1
w = 1

list = []

if len < wid:
    len = wid
    wid = len

if k < len*wid:

    if len - wid == 1:
        while (l <= wid):
            list.append(l * wid)
            l += 1

        while (w <= len - 2):
            list.append(w*len)
            w += 1
    elif len - wid == 2:
        while (l <= wid + 1):
            list.append(l * wid)
            l += 1

        while (w <= len - 3):
            list.append(w*len)
            w += 1
    elif len - wid == 3:
        while (l <= wid + 2):
            list.append(l * wid)
            l += 1

        while (w <= len - 4):
            list.append(w*len)
            w += 1
    elif len - wid == 0:
        while (l < wid):
            list.append(l * wid)
            l += 1
    print(list)

    def Ysl(x):
        for i in x:
            if i == k:
                return print("yes")
        return print("no")

    Ysl(list)
else:
    print("недопустимая величина кусочеков")
