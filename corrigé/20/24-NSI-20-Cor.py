# By ToyHugs

# Énoncé

def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return ... 

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return ... 

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(...): 
            nouvelle_image[i][j] = ... 
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 1 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(...): 
            if image[i][j] < ... : 
                nouvelle_image[i][j] = ... 
            else:
                nouvelle_image[i][j] = ... 
    return nouvelle_image

# Corrigé

# Exercice 1

import random

def lancer(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 6))

    return tab

def paire_6(tab):
    nb_6 = 0
    for nombre in tab:
        if nombre == 6:
            nb_6 += 1
    
    if nb_6 > 1:
        return True
    
    return False

# Exemples

print("Exercice 1:")

lancer5 = lancer(5)
lancer6 = lancer(6)

print(lancer5)
print(lancer6)
print(paire_6(lancer5))
print(paire_6(lancer6))
print(lancer(0))


# Exercice 2


def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            nouvelle_image[i][j] = 255 - image[i][j] 
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 1 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            if image[i][j] < seuil : 
                nouvelle_image[i][j] = 0 
            else:
                nouvelle_image[i][j] = 1
    return nouvelle_image

# Exemples

print("Exercice 2:")

img =[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

print(nombre_lignes(img)) #4
print(nombre_colonnes(img)) #5
print(negatif(img)) # [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
print(binaire(img,120)) # [[0, 0, 1, 1, 0],[0, 1, 1, 1, 0],[1, 1, 1, 0, 0],[1, 0, 0, 1, 1]]

