"""
for n in range(16):
    print(n)


for n in range(15,-1,-1):
    print(n)
"""
"""
d=int(input("valeur du début"))
f=int(input("valeur de fin"))

for n in range(d,f,+1):
    print(n)

"""
"""
d=int(input("valeur de debut"))

for n in range(d,d+11):
    print(n)
"""
"""
ex6
max=0
for n in range(5):
    nb=int(input("saisir un nombre"))
    if nb>max:
        max=nb
print("le nb max est",max)
"""
"""
valeur=0
max=0
while valeur>=0:
    valeur=int(input("saisir un nombre positif ou -1 pour "))
    if valeur>max:
        max=valeur

    print("le nombre max est",max)
"""
"""
valeur=0
somme=0
while valeur>=0:
    valeur=int(input("saisir un nombre :"))
    somme=somme+valeur
print("la somme des chiffres est ",somme)
"""

menu=0
while menu!='q':
    print("1 : charger le fichier")
    print("2 : sauvegarder le fichier")
    print("3 : afficher les données")
    print("4 : modifier les données")
    print("q : quitter")
    menu=input("votre choix ")
    if menu=='1':
        print





