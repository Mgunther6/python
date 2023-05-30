#import pygal   #question 8

coefficients=[5,5,5,5,5,5,10,10,8,10,16,16,100]
notes=[12,11,13,8,16,12,12.5,9,14,15,11,19]
matieres=["Enseignement scientifique",
            "Histoire/géographie",
            "Langue vivante A ",
            "Langue vivante B ",
            "EPS",
            "Enseignement spécialité 1ere",
            "Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2"]


def calculMoyenne(coefficients,notes):
    somme=0
    for n in range(0,len(notes)):
        somme+=coefficients[n]*notes[n]
    moyenne=somme/100
    return moyenne






def traitementBac(moyenne):
    print ("Votre moyenne est de",moyenne)
    if moyenne<8:
        print("pas de bac")
    elif 8<moyenne<10:
        print("ratrapage")
    elif 10<=moyenne<12:
        print("bac")
    elif 12<=moyenne<14:
        print("votre mention est assez bien")
    elif 14<=moyenne<16:
        print("bien")
    elif 16<=moyenne:
        print("très bien")





def rechercheNoteMin(notes):
    min=notes[0]
    for i in range(0,len(notes)):
        if notes[i]<min:
            min=notes[i]
    return min
print("la note la plus basse est",rechercheNoteMin(notes))



def rechercheNoteMax(notes):
    max=notes[0]
    for i in range(0,len(notes)):
        if notes[i]>max:
            max=notes[i]
    return max
print("la note la plus haute est",rechercheNoteMax(notes))

def rechercheNote(notes,matieres,laNote):
    compteur=0
    x=int(input("la note rechecher est:"))
    for f in range(len(notes)):
        if x==notes[f]:
            compteur+=1
            print("vous avez",x,"en",matieres[f])
            print("vous avez",x,"dans",compteur,"matières")





def changeNote(notes):
    for k in range(0,len(notes)):
        note=-1
        while note<0 or note>20:
            print("quel est votre note en",matieres[k])
            note=float(input())
        notes[k]=note




def tableauBac(coefficients,notes,matieres):
    for i in range(len(notes)):



#changeNote(notes)
moyenne=calculMoyenne(coefficients,notes)
traitementBac(moyenne)
rechercheNoteMin(notes)
rechercheNoteMax(notes)
rechercheNote(notes,matieres,12)
tableauBac(coefficients,notes,matieres)

#line_chart = pygal.HorizontalBar()
#line_chart.title = 'Notes du Bac (/20)'
#a completer question 8

#line_chart.render_to_file('notes.svg')
