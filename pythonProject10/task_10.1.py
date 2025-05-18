from PIL import Image
image = Image.open("holiday.jpg")
image.show()
cropped = image.crop((70, 0, 690, 110))
cropped.save("text.jpg")
print("Операция завершена!")