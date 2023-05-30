# Créé par MATIS.GUNTHER, le 06/04/2023 en Python 3.7

"""
tab=[18,47,8,21,34]
n=len(tab)
for i in range(1,n):
    j=i
    memoire=tab[i]
    while j>0 and memoire<tab[j-1]:
gh'te("a'        tab[j-1],tabl[j] = tab[j],tab[j-1]
        j=j-1
    tab[j]=memoire
"""

from random import randint

Tableau = [randint(0, 1000000) for i in range(1000)]
Tableau.sort(reverse=True)

nb_affectation = 0

for i in range(1,len(Tableau)):

    j=i

    encours=Tableau[i]
    nb_affectation += 1

    while (j>0) and encours<Tableau[j-1]:

        Tableau[j] = Tableau[j-1]
        nb_affectation += 1

        j-=1

    Tableau[j]=encours

print('taille n=',len(Tableau)," nb affectation =",nb_affectation)
