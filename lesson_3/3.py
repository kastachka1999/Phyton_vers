# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

#Ввод: ноутбук
#Вывод: 12

def Scrabble(cl, lang):
    count = 0
    for el in lang.keys():
        x = el.split(', ')
        for elem_cli in cl:
            for elem_obj in x:
                if (elem_cli == elem_obj):
                    count += lang[el]
    return count


def likes_spicyfood():
    spicyfood = input("ru or en?: ")
    if spicyfood == "ru":
        client = list(str(input("ввод: ")).upper())
        return print(Scrabble(client, list_ru))
    if spicyfood == "en":
        client = list(str(input("ввод: ")).upper())
        return print(Scrabble(client, list_en))


list_ru = \
    {
        'А, В, Е, И, Н, О, Р, С, Т': 1,
        'Д, К, Л, М, П, У': 2,
        'Б, Г, Ё, Ь, Я': 3,
        'Й, Ы': 4,
        'Ж, З, Х, Ц, Ч': 5,
        'Ш, Э, Ю': 8,
        'Ф, Щ, Ъ': 10
    }
list_en = \
    {
        'A, E, I, O, U, L, N, S, T, R': 1,
        'D, G': 2,
        'B, C, M, P': 3,
        'F, H, V, W, Y': 4,
        'K': 5,
        'J, X': 8,
        'Q, Z': 10,
    }

likes_spicyfood()
