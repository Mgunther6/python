# Créé par MATIS.GUNTHER, le 07/03/2023 en Python 3.7
"""
d = { 'nom':'Dupuis' , 'prenom':'Jacque', 'age':30}
d['prenom']='jacques'
print(d['prenom'], d['nom'], 'a', d['age'], 'ans')
print (d.items())
print(d.values())
print(d.keys())
print (d)
"""
"""
courses ={'pain':4, 'riz':9, 'tomates':7}
courses['tomates']+=1
for nom, num in courses.items():
    print(nom, '->', num)
"""
"""
def occurrences(chaine) :
    D = {}
    for caractere in chaine :
        if caractere in D.keys():
            D[caractere]+=1
        else:
            D[caractere]=1
    return D


print(occurrences('tortue'))
"""
"""
pieces=[500,200,100,50,20,10,5,2,1]
somme=780
def renduMonnaie(somme,pièces):
    choisies={}
    for p in pièces:
        choisies[p]=0
        while somme>=p:
            somme=somme-p
            choisies[p]+=1
    return choisies
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
somme=780
pieces=[500,200,100,50,20,10,5,2,1]
def renduMonnaie(somme,pieces):
    choisies={}
    for p in pieces:
        nb=somme//p
        choisies[p]=nb
        somme=somme-nb*p
    return choisies
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))