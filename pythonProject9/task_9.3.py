from PIL import Image, ImageFilter
import os

directory = 'img_filters' # создание папки
os.makedirs(directory, exist_ok=True)

files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for file_name in files:

    img_path = file_name
    with Image.open(img_path) as img:

        filter_img = img.filter(ImageFilter.CONTOUR)  # фильтр

        new_file = f'filter_{file_name}' #новое имя файла
        filter_img.save(os.path.join(directory, new_file))

