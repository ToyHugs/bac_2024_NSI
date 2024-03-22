# By ToyHugs

# Énoncé

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = ... 

    for x in tab:
        if x < ... or x >... or ...: 
            return False
        ... .append(...) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert ... 
    n = len(ordre)
    nb = 0
    if ordre[...] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < ...: 
        if ... not in [-1, 1]: # l'écart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != ...: # le dernier n'est pas n 
        nb = nb + 1
    return nb

# Corrigé

# Exercice 1

def max_et_indice(tab):
    '''
    Renvoie le maximum et l'indice de ce maximum dans tab
    '''
    max = tab[0]
    indice = 0
    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
            indice = i
    return max, indice

'''>> max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
(9, 3)
>>> max_et_indice([-2])
(-2, 0)
>>> max_et_indice([-1, -1, 3, 3, 3])
(3, 2)
>>> max_et_indice([1, 1, 1, 1])
(1, 0)
2 / 4'''

# Exemples

print("Exercice 1 : Exemples")

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])) # (9, 3)

print(max_et_indice([-2])) # (-2, 0)

print(max_et_indice([-1, -1, 3, 3, 3])) # (3, 2)

print(max_et_indice([1, 1, 1, 1])) # (1, 0)

# Exercice 2

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = [] # Liste vide pour stocker les entiers vus

    for x in tab:
        if x < 1 or x > n or x in vus: # Si x n'est pas dans l'intervalle [1, n] ou s'il a déjà été vu
            return False
        vus.append(x) # On ajoute x à la liste des entiers vus
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre) # On vérifie que ordre est un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < n - 1: # On parcourt les éléments de ordre sauf le dernier 
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'écart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n 
        nb = nb + 1
    return nb

# Exemples

print("Exercice 2 : Exemples")

print(est_un_ordre([1, 6, 2, 8, 3, 7])) # False

print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9])) # True

print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9])) # 4

print(nombre_points_rupture([1, 2, 3, 4, 5])) # 0

print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5])) # 7

print(nombre_points_rupture([2, 1, 3, 4])) # 2