import functions as fn


def exit():
    for i in obj_menu:
        print(i[0], i[1])
    global a
    a = int(input("num?: "))
    for i in obj_menu:
        print(i[0], i[1])


obj_menu = [
    [1, "Вывод автобусов"],
    [2, "Добавление автобуса"],
    [3, "Вывод водителей"],
    [4, "Добавление водителей"],
    [5, "Вывод маршрута"],
    [6, "Добавление маршрута"],
    [7, "ТЕкущая обстановка"],
    [8, "ВЫход"]
]

exit()

if a == 1:
    fn.All_buses("buses")

if a == 2:
    actions = [
        [1, 'Добавить новый автобус?'],
        [2, 'Изменить старый ?'],
        [3, 'Выход']
    ]
    print()
    for i in actions:
        print(i[0], i[1])
    k = int(input("дуйствие: "))
    if k == 3:
        exit()

    fn.Push_bus("buses", k)

if a == 3:
    fn.PrintRiders("riders")

if a == 4:
    actions = [
        [1, 'Добавить нового водителя  '],
        [2, 'Изменить статус ?  '],
        [3, 'Выход']
    ]
    print()
    for i in actions:
        print(i[0], i[1])
    k = int(input("действие: "))
    if k == 3:
        exit()

    fn.Push_bus("riders", k)

if a == 5:
    fn.PrintRoutes("route")

if a == 6:
    # аналогично с предыдущими
    exit()

if a == 7:
    fn.Tek("buses", "riders", "route")
