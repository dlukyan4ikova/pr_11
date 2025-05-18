from PIL import Image, ImageDraw, ImageFont
import random

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

holidays = {
    "1": "День рождение",
    "2": "День тортика",
    "3": "Пасха"
}

for key in holidays:
    print(key, " - ", holidays[key])

n = input("Введите номер открытки для просмотра: ")

if n in holidays:
    filename = "pic" + n + ".jpg"
    otkryitka = Image.open(filename)

    recipient_name = input("Введите имя того, кого вы хотите поздравить: ")

    draw = ImageDraw.Draw(otkryitka) # объект для рисования на открытке

    # Загружаем шрифты (можно указать путь к своим шрифтам)
    try:
        font1 = ImageFont.truetype("arial.ttf", 56)
        font2 = ImageFont.truetype("arial.ttf", 56)
    except IOError:
        font1 = ImageFont.load_default()
        font2 = ImageFont.load_default()


    greeting_text = f"{recipient_name}, поздравляю!"

    text_bbox = draw.textbbox((0, 0), greeting_text, font=font1)
    text_width = text_bbox[2] - text_bbox[0]  # Ширина
    text_height = text_bbox[3] - text_bbox[1]  # Высота

    text_x = (otkryitka.width - text_width) / 2 # ставим текст по центру вверху
    text_y = 20  # Отступ вверху

    draw.text((text_x, text_y), greeting_text, fill=random_color(), font=font1) # текст с рандом текстом

    new_otkryitka = f"pozdravlenie_{recipient_name}.png"
    otkryitka.save(new_otkryitka)

    print(f"Открытка сохранена как '{new_otkryitka}'")
else:
    print("Ошибка! Введите число от 1 до 3")
