#import pillow as pillow

#pip3 install pillow
from PIL import Image
def z1(n):
    im=Image.open('0.jpg')
    im.show()
    print(" Ширина: ", im.size[0], "\n", "Высота: ", im.size[1],"\n", "Формат: ", im.format,"\n", "Цветовая модель: ", im.mode )
    return ""
def z2(n):
    im=Image.open('0.jpg')
    im2=im.reduce(3)
    im2.save('little 0.jpg')
    im3=im.transpose(Image.FLIP_LEFT_RIGHT)
    im4=im.transpose(Image.FLIP_TOP_BOTTOM)
    im3.save('LR 0.jpg')
    im4.save('TB 0.jpg')
    return ""
def z3(n):
    for i in range (1,6):
        m=str(i)+'.jpg'
        im=Image.open(m)
        imm=im.convert('L')
        imm.save('new '+m)
    return ""
def z4(n):
    wat=Image.open('wat.png')
    im=Image.open('0.jpg')
    wat=wat.reduce(4)
    wat=wat.transpose(Image.FLIP_TOP_BOTTOM)
    im.paste(wat, (50,50), wat )
    im.save('wat firret.png')
    return ""
z1(" ")
z2(" ")
z3(" ")
z4(" ")

