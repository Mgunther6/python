
"""
"exercice 1)"
def renverse(mot):
    nouveaumot=""
    for i in range (len(mot)):
        nouveaumot+=mot[-i-1]
    return nouveaumot
print(renverse("informatique") )
"""

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,100)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1
    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore "))
        else:
            nb_test = int(input("Trop grand ! Testez encore "))
    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)

plus_ou_moins()

"""
def recherche(caractere,chaine):
    compteur=0
    for i in range(len(chaine)):
        if chaine[i]==caractere:
            compteur+=1
    return compteur

print(recherche('e', "sciences")) #2
print(recherche('i', "mississippi")) #4
print(recherche('a', "mississippi"))#0
"""