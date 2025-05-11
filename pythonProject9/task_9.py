from PIL import Image

image = Image.open("frog.jpg")

print(f"Размер: {image.size} ")
print(f"Формат: {image.format} ")
print(f"Цветовая модель: {image.mode} ")
image.show()
