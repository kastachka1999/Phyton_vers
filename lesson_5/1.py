file = 'c:/Users/User/Desktop/Phyton/lesson_5/text.txt'


def ReadAllFile(nameFile):
    with open(nameFile, 'r', encoding='utf-8') as g:
        return print(g.read())


def GetList(nameFile):
    list = []
    with open(nameFile, 'r+', encoding='utf-8') as g:
        for string in g:
            b = string.split()
            list.append(b[0].split(','))
    return list


def GetVocabulary(listName):
    iter = 0
    result = []
    for i in listName:
        id = iter
        Name = i[0]
        Surname = i[1]
        Lastname = i[2]
        Number = i[3]
        d = dict(id=id, Name=Name, Surname=Surname,
                 Lastname=Lastname, Number=Number)
        result.append(d)
        iter += 1
    return result


def getForName(kontakts):
    name = input('name ')
    names = []
    for item in kontakts:
        if item[1] == name:
            names.append(item)
    if len(names) == 0:
        print('таких нет')
    else:
        for elem in names:
            print(
                f'\nSurname: {elem[0]}\nName: {elem[1]}\nLastname: {elem[2]}\nNumber: {elem[3]}')


def getForNumber(kontakts):
    number = input("number ")
    numbers = []
    for item in kontakts:
        if item[3] == number:
            numbers.append(item)
    if len(numbers) == 0:
        print('таких нет')
    else:
        for elem in numbers:
            print(
                f'\nName: {elem[0]}\nSurname: {elem[1]}\nLastname: {elem[2]}\nNumber: {elem[3]}')


def PushKontakt(nameFile):
    Name = input('name ')
    Surname = input('surname ')
    Lastname = input('lastname ')
    Number = input('number ')
    with open(nameFile, 'a', encoding='utf-8') as g:
        g.writelines(f"\n{Surname},{Name},{Lastname},{Number}")


def Delete(nameFile):
    Name = input('name ')
    Surname = input('surname ')
    lis = GetList(nameFile)
    i = 0
    for elem in lis:
        if elem[0] == Surname and elem[1] == Name:
            lis.pop(i)
        i += 1
    if len(lis) == len(GetList(nameFile)):
        return print("таких нет")
    else:
        with open(nameFile, 'w+', encoding='utf-8') as g:
            for elem in lis:
                g.writelines(f"{elem[0]},{elem[1]},{elem[2]},{elem[3]}\n")
            print('deleted')


def ChangeNum(nameFile, myList):
    Surname = input('surname ')
    NewNumber = input('new number ')
    for item in myList:
        if item[0] == Surname:
            item[3] = NewNumber
    with open(nameFile, 'w+', encoding='utf-8') as g:
        for elem in myList:
            g.writelines(f"{elem[0]},{elem[1]},{elem[2]},{elem[3]}\n")
        print('will change')


# ReadAllFile(file) чтение файла

print('''Введите номер действия:
      1 - Показать все записи
      2 - Найти запись по вхождению частей имени
      3 - Найти запись по телефону
      4 - Добавить новый контакт
      5 - Удалить контакт
      6 - Изменить номер телефона у контакта
      7 - Выход''')

num = int(input('№'))


def Switch(a):
    if a == 1:
        ReadAllFile(file)
    if a == 2:
        getForName(GetList(file))
    if a == 3:
        getForNumber(GetList(file))
    if a == 4:
        PushKontakt(file)
    if a == 5:
        Delete(file)
    if a == 6:
        ChangeNum(file, GetList(file))
    if a == 7:
        print('back')


Switch(num)
