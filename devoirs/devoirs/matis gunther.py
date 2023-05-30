
terminaisons=['e','es','e','ons','ez','ent']
pronoms=['je','tu','il/elle','nous','vous','ils/elles']
voyelles=['a','e','i','o','u','y']


verbe=str(input("votre chaine ?"))
if verbe=="aller":
    print("impossible")
elif verbe[:-2]!='re':
    print("pas possible")
else:
    for n in range(len(pronoms)):
        print(pronoms[n],verbe[:-2]+terminaisons)

"""
liste=["bonjour","ici","fleur","fleuve","informatique"]
alphabet=("a","b","d","e","f","g","h","i","j","q","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
lettre=alphabet
def comptelettre(lettre,liste):
    return liste.count(lettre)
motLePlusLong=most:alphabet
print(motLePlusLong(liste))
"""