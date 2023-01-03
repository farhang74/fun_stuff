from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt



size = 200, 200
myfont = ImageFont.truetype("/home/farhang/.fonts/truetype/Shabnam/shabnam-font-master/dist/Shabnam-Thin.ttf", 35)

text = "FARHANG"
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, size[1]/2), text, "white", align='center', font=myfont)
pixels = np.array(img, dtype=np.uint8)


plt.imshow(pixels)
plt.show()