def f(x):
    return(x*x-3*x+4)

def imc(masse,taille):
    #calcul du rapport
    rapport=masse/(taille**2)
    #renvoi de l'arrondi à 0.1
    return(round(rapport,2))

#exercice 1 question 1
def d(v):
    return(0.01*v**2+0.28*v)

#exercice 1 question 2
def c(x,y):
    return(x*x+y*y)

#exrcice 2 question 1
def soldes(prix,taux):
    reduc=prix*taux
    prixsolde=prix-reduc
    return(reduc,prixsolde)

#exercice 2 question 4
def augmentation(prix, taux):
    augmentation=prix*taux
    prixsolde=prix+augmentation
    return (augmentation,prixsolde)

#exercice 3 question 1
def montant(HT,TVA):
    TTC=HT*TVA+HT
    return(TTC,TVA)

#exercice 4 question 1
from math import*
def hyp(a,b):
    c=a**2+b**2
    return(sqrt(c))

#exercice 4 question 2
from math import*
def perimetre(a,b):
    c=a**2+b**2
    sqrt(c)
    return(a+b+c)





