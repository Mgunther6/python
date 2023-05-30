# Créé par MATIS.GUNTHER, le 08/12/2022 en Python 3.7
"""
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>='' and texte[c]<='z':
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))
"""
"""
def insertionTexte(texte):
    nouveauTexte:' '
    for i in range(len(texte)-1):
        nouveauTexte+=texte[i]+'*'
    nouveauTexte+=texte[-1]
    return nouveauTexte


texte=str(input("votre texte ?"))
print(insertionTexte(texte))
"""
def inversionMot(texte):
    nouveauTexte=''
    for i in range(len(texte)-1):



