from PIL import Image

holidays={"1":"День рождение","2":"День тортика","3":"День плохого интернета"}
for key in holidays:
    print(key, " - ", holidays[key])

n = input("Введите номер открытки для просмотра: ")

if n in holidays:
    filename = "pic"+n+".jpg"
    otkryitka = Image.open(filename)
    otkryitka.show()
else:
    print("Ошибка! Введите число от 1 до 3")