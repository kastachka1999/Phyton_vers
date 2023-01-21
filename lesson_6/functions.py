import json
import random
# получает име файла и преобразовывает в обьект


def read(data):
    with open(f'c:/Users/User/Desktop/Phyton/lesson_6/{data}.json', 'r', encoding='utf8') as file:
        obj = json.load(file)
        return obj


# получает измененный обьект и записывает в соответствующий файл
def write_all(obj, data):
    with open(f'c:/Users/User/Desktop/Phyton/lesson_6/{data}.json', 'w', encoding='utf8') as file:
        json_object = json.dump(obj, file)


def All_buses(data):  # вывод автобусов
    lis = read(data)
    for i in lis:
        print(f'автобус {i["name"]} номер {i["num"]}')


def Push_bus(data, num):  # добавление автобуса
    if num == 1:  # новый
        name = input("марка ")
        num = input("номер ")
        status = input("статус ")
        id = random.randint(10, 99)
        obj_js = read(data)
        for el in obj_js:  # проверка
            if el["id"] == id:  # нет схожего id
                id = random.randint(100, 999)
            if el["num"] == num:
                c = random.randint(100, 999)
                print(f"такой номер уже есть, свободен номер {c} ?")
                num = c
        obj_js.append(dict(id=id, name=name, num=num, status=status))
        write_all(obj_js, data)

    if num == 2:  # изменение статуса
        num_search = int(input("какой номер автобуса?  "))
        obj_js = read(data)
        for el in obj_js:
            if el["num"] == num_search:
                sts = str(input("введите статус  "))
                el["status"] = sts
        write_all(obj_js, data)


def PrintRiders(data):  # вывод водителей
    l = read(data)
    for i in l:
        print(f"водитель {i['name']} статус {i['sts']} ")


def Push_bus(data, k):
    if k == 1:  # новый
        name = input("име ")
        status = input("статус ")
        id = random.randint(10, 99)
        obj_js = read(data)
        for el in obj_js:  # проверка
            if el["id"] == id:  # нет схожего id
                id = random.randint(100, 999)

        obj_js.append(dict(id=id, name=name, status=status))
        write_all(obj_js, data)
    if k == 2:
        num_sts = str(input("какой статус  "))
        obj_js = read(data)
        for el in obj_js:
            if el["sts"] == num_sts:
                sts = str(input("введите статус  "))
                el["sts"] = sts
        write_all(obj_js, data)


def PrintRoutes(data):
    l = read(data)
    for i in l:
        print(
            f"водитель {i['rider_id']} на маршруте {i['name']} на автобусе {i['bus_id']}")


def Tek(bus, rid, rou):
    ob_bus = read(bus)
    ob_rid = read(rid)
    ob_rou = read(rou)
    for el in ob_rou:
        i = 0
        print(f"маршрут {el['name']}")
        while i < len(ob_bus):

            if el["bus_id"] == ob_bus[i]['id']:
                print(f"автобус {ob_bus[i]['name']}")
            if el["rider_id"] == ob_rid[i]['id']:
                print(f"водитель {ob_rid[i]['name']} \n")

            i += 1

    print()
