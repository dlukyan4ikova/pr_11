def spravochnik_stran(vvod, slovar):
    if vvod in slovar:  # Проверка на ввод страны
        return f"Столица {vvod}: {slovar[vvod]}"

    for key, value in slovar.items():  # Проверка на ввод столицы
        if value == vvod:
            return f"Страна с столицей {vvod}: {key}"

    return "Страна или столица не найдены"


def kolvo_bukv(vvod):
    bukvi = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }

    kolvo = 0
    word = vvod.upper()

    for letter in word:
        kolvo += bukvi.get(letter, 0)

    return kolvo


# Основной код
slovar = {
    'Австрия': 'Вена',
    'Франция': 'Париж',
    'Румыния': 'Бухарест',
    'Ирландия': 'Дублин',
    'Россия': 'Москва'
}

while True:

    e = input("Введите номер задания (1 или 2), или q для выхода: ")

    if e == "1":
        vvod = input("Введите страну или столицу: ")
        rez = spravochnik_stran(vvod, slovar)
        print(rez)

    elif e == "2":
        vvod = input("Введите слово: ")
        total_value = kolvo_bukv(vvod)
        print(f"Стоимость слова '{vvod}': {total_value} очков")

    elif e.lower() == "q":
        print("Выход из программы.")
        break

    else:
        print("Некорректный номер задания. Пожалуйста, введите 1 или 2.")
