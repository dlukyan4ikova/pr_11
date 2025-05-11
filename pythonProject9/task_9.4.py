from PIL import Image

voda_znak = Image.open("voda_znak.png")

image = Image.open("manhva.jpg")
image.paste(voda_znak, (120, 420), voda_znak)
image.save("voda_znak(new).png")