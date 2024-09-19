from PIL import Image


image = Image.open("monro.jpeg")
red,green,blue = image.split()
img_1 = red
coor_1 = img_1.crop((100,0,img_1.width, img_1.height))
img_2 = red
coor_2 = img_2.crop((50,0,img_1.width-50, img_1.height))
image_1 = Image.blend(coor_1, coor_2, 0.5)

img_3 = blue
coor_3 = img_3.crop((0,0,img_1.width-100, img_1.height))
img_4 = blue
coor_4 = img_4.crop((50,0,img_1.width-50, img_1.height))
image_2 = Image.blend(coor_3, coor_4, 0.5)

img_5 = green
image_3 = img_5.crop((50,0,img_1.width-50, img_1.height))
style = Image.merge("RGB",(image_1,image_3,image_2))
style.show()

# style.thumbnail((80,70))
# style.save("80x7.jpg")





