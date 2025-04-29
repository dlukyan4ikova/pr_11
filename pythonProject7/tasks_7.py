
import random
# задача 1
def guess_number():

    numbers = random.sample(range(11), 5)

    vvod = int(input("Введите число от 0 до 10: "))

     #Проверка наличия числа в списке
    if vvod in numbers:
        vyvod = "Поздравляю, Вы угадали число!"
    else:
        vyvod = "Нет такого числа!"

    print(f"Исходный список: {numbers}")
    print(f"Ваше число: {vvod}")
    print(vyvod)
#guess_number()

# задача 2
def povtorenie():
    spisok = list(random.randint(1, 10) for _ in range(10))
    print(f"Исходный список: {spisok}")

    ne_povtor = set()  # множество для хранения уникальных элементов
    povtor = {}

    for chislo in spisok:
        if chislo not in ne_povtor:
            ne_povtor.add(chislo)
            kolvo_povtor = spisok.count(chislo)
            if kolvo_povtor > 1:
                povtor[chislo] = kolvo_povtor

    if povtor:
        for chislo, kolvo_povtor in povtor.items():
            print(f"Число {chislo} встречается в списке {kolvo_povtor} раз(а).")
    else:
        print("В данном списке повторений нет")

#задача 3
def get_weekend_and_workdays():
    days_of_week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

    while True:
        try:
            num_weekends = int(input("Сколько выходных дней вы хотите (от 0 до 7)? "))
            if 0 <= num_weekends <= 7:
                break
            else:
                print("Пожалуйста, введите число от 0 до 7.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    # разделение кортежа на выходные и рабочие дни
    weekends = days_of_week[-num_weekends:]  # Срез выхов
    workdays = days_of_week[:-num_weekends]
    return weekends, workdays
# задание 4
def familii():
    my_group = ["Капкайкина", "Малахов", "Ершов", "Гиносян", "Шахбалаева", "Кюлян", "Коновальчиков", "Сухопар",
           "Огородникова", "Мельников"]
    not_my_group = ["Пивоваров", "Виноделов", "Сыроедова", "Мясорубов", "Запеканкина", "Лукова", "Пирожков", "Сметанкин", "Борщев",
          "Хлебушкина"]
    comm1 = tuple(random.sample(my_group, 5))
    comm2 = tuple(random.sample(not_my_group, 5))
    sport_comm = comm1 + comm2

    print(f"Моя группа: {my_group}\nЛевая группа: {not_my_group}\nКоманда: {sport_comm}\nДлина кортежа: {len(sport_comm)} ")

    sortirovka = tuple(sorted(sport_comm))
    print("Сортировка команды по алфавиту:", sortirovka)

    Ivanov = sport_comm.count("Иванов")
    if Ivanov > 0:
        print(f"Иванов есть в команде и встречается {Ivanov} раз")
    else:
        print("К сожалению, Иванова нет в команде:(")

e = int(input("Введите номер задания:"))
if e==1:
    guess_number()
elif e==2:
    povtorenie()
elif e == 3:
    weekends, workdays = get_weekend_and_workdays()
    print("Выходные дни:", weekends)
    print("Рабочие дни:", workdays)
elif e ==4:
    familii()






