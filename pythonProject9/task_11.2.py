from PIL import Image
import os
from pathlib import Path

input_directory = 'old_file'

for file_name in os.listdir(input_directory):

    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_directory, file_name)

        image = Image.open(img_path)
        print(f"Файл: {file_name}")
        print(f"Размер: {image.size}")
        print(f"Формат: {image.format}")
        print(f"Цветовая модель: {image.mode}")
        image.show()
print("Обработка завершена!")
