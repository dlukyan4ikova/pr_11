from datetime import datetime

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

vvod = input("Введите дату в формате дд.мм.гггг: ")
rez = magic(vvod)

if rez is not None:
    if rez:
        print("Дата является магической")
    else:
        print("Дата не является магической")

