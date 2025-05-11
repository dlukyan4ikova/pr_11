from PIL import Image

image = Image.open("selfi.jpg")
image.show()
red_img = image.reduce(3)
zer_horiz = image.transpose(Image.FLIP_LEFT_RIGHT)
zer_vertik = image.transpose(Image.FLIP_TOP_BOTTOM)

red_img.save("micro_selfi.png")
zer_horiz.save("horiz_selfi.png")
zer_vertik.save("vertik_selfi.png")
