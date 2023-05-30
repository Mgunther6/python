from pylab import *
def calcul_nb_pliages(hauteur):
    EPAISSEUR_FEUILLE=0.0001
    somme_hauteur=EPAISSEUR_FEUILLE
    pliages=0
    while somme_hauteur<hauteur:
        somme_hauteur=somme_hauteur*2
        pliages+=1
        print(somme_hauteur)
        x.append(somme_hauteur)
        y.append(pliages)
    return pliages
x=[]
y=[]
print(calcul_nb_pliages(1.6))
plot(x, y)
show()