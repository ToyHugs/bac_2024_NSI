# By ToyHugs

# Énoncé

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < ... and a > ...: 
        tab_a[i] = ... 
        tab_a[i+1] = a
        i = ... 
    return tab_a

# Correction

# Exercice 1

def recherche(elt, tab):
    """
    Renvoie l'indice de l'élément elt dans le tableau tab ou None si l'élément n'est pas présent.
    """
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return None

# Exemples

print("Exercice 1 :")

print(recherche(1, [2, 3, 4])) # None
print(recherche(1, [10, 12, 1, 56])) # 2
print(recherche(50, [1, 50, 1])) # 1
print(recherche(15, [8, 9, 10, 15])) # 3

# Exercice 2

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]:
        tab_a[i] = tab[i]
        tab_a[i+1] = a
        i = i + 1
    return tab_a

# Exemples

print("Exercice 2 :")

print(insere([1, 2, 4, 5], 3)) # [1, 2, 3, 4, 5]
print(insere([1, 2, 7, 12, 14, 25], 30)) # [1, 2, 7, 12, 14, 25, 30]
print(insere([2, 3, 4], 1)) # [1, 2, 3, 4]
print(insere([], 1)) # [1]
