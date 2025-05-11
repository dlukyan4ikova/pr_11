def delenie_sto():
    try:
        vvod = input("Введите число: ")
        chislo = int(vvod)
        rez = 100 / chislo
        print(f" 100 / {chislo} = {rez}")
    except ValueError:
        print("Ошибка! Введите числовое значение.")
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль. Введите другое число.")

delenie_sto()



