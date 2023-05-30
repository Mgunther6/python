""" ex1
def texte():
    print("bonjour")
texte()

"""
""" ex2
def texte(prenom):
    print("bonjour",prenom)
texte("matis")
"""
""" ex3
def somme(a,b):
    somme=a+b
    return somme
print(somme(3,5))
"""
""" ex4
def calculsurface(longueur,largeur):
    surface=longueur*largeur
    return surface
print(calculsurface(10.5,2))
"""
""" ex 5
def calculFormule(x):
    y=2*x**2-4*x+3
    return y
print(calculFormule(3.14))
"""
""" ex9
def triangle(hauteur,largeur):
    for h in range(1,hauteur+1):
        largeur=largeur+1
        for l in range(1,largeur+1):
            print("*",end="")
        print()
triangle(10,0)
"""
from math import pi
def volume(rayon):
    vol=(4*pi*rayon**3)/3
    return(vol)
print(volume)

volume(10)
