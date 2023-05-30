# Créé par matis.gunther, le 22/11/2022 en Python 3.7
"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))



largeur,hauteur=img.size
draw=ImageDraw.Draw(img)
draw.line((0,0,largeur,hauteur),fill=(0,255,0))

draw.line((10,20,100,200),fill=(255,0,0))
img.show()
"""
"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    for x in range(nbDroites):
        draw.line((x*ecart,0,xnbDroites*ecart,hauteur),fill=(0,255,0))


traceDroite(10,20)

img.show()
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)


def tracecible(nbcercle):

        cercle(128,128,60(0,0,255))
        cercle(128,128,50(255,0,0))
        cercle(128,128,30(255,255,0))



tracecible(3)
img.show()
