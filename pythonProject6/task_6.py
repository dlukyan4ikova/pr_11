
def delenie(chislo): #1

    if chislo % 3 == 0:
        print("Это число делится на 3")
    else:
        print("Это число не делится на 3")

#
def delenie_sto(): #2
    try:
        vvod = input("Введите число: ")
        chislo = int(vvod)
        rez = 100 / chislo
        print(f" 100 / {chislo} = {rez}")
    except ValueError:
        print("Ошибка! Введите числовое значение.")
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль. Введите другое число.")
#
from datetime import datetime #3
def magic(data_stroka):
    try:
        data = datetime.strptime(data_stroka, "%d.%m.%Y") # преобразование даты в строку

        day = data.day
        month = data.month
        year = data.year

        product = day * month

        posled_ch = year % 100
        return product == posled_ch

    except ValueError:
        print("Ошибка! Некорректная дата. Пожалуйста, используйте формат дд.мм.гггг.")
        return None

#
def luck_ticket(nomer_tick):
# Проверяем, что длина номера четная и состоит только из цифр
    if len(nomer_tick) % 2 != 0 or not nomer_tick.isdigit(): # проверка строки на четность и числа
        return "Ошибка! Введите номер билета с четным количеством цифр"

    half_length = len(nomer_tick) // 2 # середина номера

    first_polovina = sum(int(digit) for digit in nomer_tick[:half_length])
    second_polovina= sum(int(digit) for digit in nomer_tick[half_length:])

    if first_polovina == second_polovina:
        return "Данный билет - счастливый :)"
    else:
        return "Данный билет - не счастливый :("

e = int(input("Введите номер задания: "))
if e==1:
    proverka = int(input("Введите число для проверки: "))
    delenie(proverka)
elif e==2:
    delenie_sto()
elif e==3:
    vvod = input("Введите дату в формате дд.мм.гггг: ")
    rez = magic(vvod)

    if rez is not None:
        if rez:
            print("Дата является магической")
        else:
            print("Дата не является магической")
elif e ==4:
    vvod = input("Введите номер билета (6 цифр): ")
    rez = luck_ticket(vvod)
    print(rez)
