﻿# Programme exemple_1.py
"""
new_message =""                   # initialise new_message avec un message vide

message = input("Veuillez saisir un texte en MAJUSCULE et terminer par ENTER")

print("Vous avez saisi ",message) # Affiche le message saisi

for n in message:
    if ord(n)>=65 and ord(n)<=90:           # pour chaque caractère n du message saisi (de la chaine message)
        code_initial = ord(n)                   # code_initial prend le code (Unicode) du caractère courant (n)

        code_minuscule = code_initial + 32      # calcul le code correspondant au caractère minuscule

        car_minuscule = chr(code_minuscule)     # car_minuscule prend le caractère/symbole correspondant
                                            # à la variable code_minuscule

        print(car_minuscule)                    # affiche le caractère obtenu

        new_message = new_message + car_minuscule # ajoute le caractère obtenu à new_message
    else:
        code_initial = ord(n)                   # code_initial prend le code (Unicode) du caractère courant (n)

        code_minuscule = code_initial      # calcul le code correspondant au caractère minuscule

        car_minuscule = chr(code_minuscule)     # car_minuscule prend le caractère/symbole correspondant
                                            # à la variable code_minuscule

        print(car_minuscule)                    # affiche le caractère obtenu

        new_message = new_message + car_minuscule

print (new_message) # Affiche le nouveau message
"""
import os
fichier=open("texte.txt","w")
fichier.write("bonjour\n")
fichier.write("salut")
fichier.close()
