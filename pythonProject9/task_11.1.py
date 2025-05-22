from PIL import Image, ImageFilter
import os
from pathlib import Path

old_directory = 'orig_img'
new_directory = 'filter_img'

Path(new_directory).mkdir(parents=True, exist_ok=True)


for file_name in os.listdir(old_directory):
    if file_name.endswith('.jpg'):  # Обработка JPG файлов
        img_path = os.path.join(old_directory, file_name)  # Полный путь к изображению

        with Image.open(img_path) as img:
            filter_img = img.filter(ImageFilter.CONTOUR)  # фильтр

            new_file_name = f'filter_{file_name}'  # Новое имя файла
            filter_img.save(os.path.join(new_directory, new_file_name))  # Сохраняем изображение

print("Обработка завершена!")
