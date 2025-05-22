import csv

def Raschet_csv(csv_filepath):
    try:
        total_sum = 0
        shopping_list = []
        csvfile = open(csv_filepath)
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = row['Продукт']
            quantity = int(row['Количество'])
            price = int(row['Цена'])
            cost = quantity * price
            total_sum += cost
            shopping_list.append(f"{product} - {quantity} шт. за {price} руб.")
            csvfile.close()
            print("Нужно купить:")
            for item in shopping_list:
                print(item)
            print(f"Итоговая сумма: {total_sum} руб.")
    except FileNotFoundError:
        print(f"Ошибка: Файл {csv_filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке CSV: {e}")
Raschet_csv("shopping_list.csv")
