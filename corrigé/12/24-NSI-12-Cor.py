# By ToyHugs

# Énoncé

'''
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, ...) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ... 

    while nb_mystere != ... and compteur < ...: 
        compteur = compteur + 1
        if nb_mystere ... nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", ...) 
        print("Nombre d'essais: ", ...) 
    else:
        print ("Perdu ! Le nombre était ", ...) 
'''

# Correction

# Exercice 1

def tri_selection(tab):
    '''Trie un tableau par ordre croissant en utilisant le tri par sélection'''
    for i in range(len(tab)):
        mini = i # On suppose que le minimum est le premier élément
        for j in range(i+1, len(tab)):
            if tab[j] < tab[mini]: # Si on trouve un élément plus petit que le minimum actuel
                mini = j # On met à jour l'indice du minimum
        tab[i], tab[mini] = tab[mini], tab[i] # On échange le minimum avec l'élément actuel grâce au tuple
    return tab

# Exemples

print("Exercice 1 :")

print(tri_selection([1, 52, 6, -9, 12])) # [-9, 1, 6, 12, 52]

# Exercice 2

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99) # On génère un nombre aléatoire entre 1 et 99 INCLUS
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0 # On initialise le compteur à 0

    while nb_mystere != nb_test and compteur < 10: # On continue tant que le nombre mystère est différent du nombre testé et que le compteur est strictement inférieur à 10 
        compteur = compteur + 1
        if nb_mystere > nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere) 
        print("Nombre d'essais: ", compteur) 
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)

# Exemple

print("Exercice 2 :")
plus_ou_moins() # Have fun !