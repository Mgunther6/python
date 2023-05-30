"""
def afficheTuple(tuple):

    prenon,nom,adresse,codePostal,ville=tuple
    print("prenom",prenom)
    print("nom",nom)
    print("code postal",codePostal)
    print("adresse",codePostal)
    print("ville",ville)

tuple=('bruce','wayne','3 impasse de la chauve souris','72000','le mans')
print(tuple)
"""
"""
def calcul(x,coefficientsDroite=tuple):
    a,b=coefficientsDroite
    y=a*x+b
    return(y)
coefficient=(2,1)
print(calcul)
"""
"""
from math import sqrt
def distance(ptA,ptB):
    xA,yA=ptA
    xB,yB=ptB
    AB=sqrt((xB-xA)**2+(yB-yA)**2)
    return AB
pointA=(1,1)
pointB=(2,2)
print(distance(pointA,pointB))
"""
"""
def rechercheMin(liste):
    min=liste[0]
    for indice in range(1,len(liste)-1):
        if liste[indice]<min:
            min=liste[indice]
        return min
lst=[20,8,9,2,35,49]
print(rechercheMin(lst))
"""
"""
def rechercheMax(lst):
    max=lst[0]
    return max
lst=[20,8,9,2,35,49]
print(rechercheMax(lst))
"""
"""
def somme(lst):
    total=0
    for n in range(len(lst)):
        total=total+lst[n]
    return total
lst=[20,8,9,2,35,49]
print(somme(lst))
"""
"""
def moyenneVersion1(liste):
    total=0
    for n in range(len(lst)):
        moyenneVersion1=total+lst[n]
    return moyenneVersion1
lst=(20,8,9,2,35,49)
print(moyenneVersion1(lst))
"""

def moyenneVersion1(liste):
    total=0
    for n in range(len(lst)):
        moyenneVersion1=total+lst[n]
    return moyenneVersion1
lst=(20,8,9,2,35,49)
print(moyenneVersion1(lst))
