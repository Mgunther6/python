# Créé par MATIS.GUNTHER, le 15/12/2022 en Python 3.7
"""
def insertionTexte(texte):
    nouveauTexte=''
    for i in range(len(texte)-1):
        nouveauTexte+=texte[i]+'*'
    nouveauTexte+=texte[-1]
    return nouveauTexte
texte=str(input("votre texte"))
print(insertionTexte(texte))
"""
"""
chaine=str(input("chaine"))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]
print(chaine,total)
"""
"""
chaine=str(input("chaine"))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]
print(chaine,total)
if total==chaine:
    print("true")
else:
    print("false")
"""
def codecesar(phrase,cle):
    total=""
    for i in range(0,len(phrase)):
        ascii=ord(phrase[i])
        conv=ascii-65+cle
        caract=chr(conv+65)
        total+=caract+""
    return total
cle=int(input("clef"))
phrase=str(input("phrase:"))
print(codecesar(phrase,cle))