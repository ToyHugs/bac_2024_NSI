# By ToyHugs

# Énoncé
def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = ... 
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = ... 
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > ... and valeur_insertion < tab[...]: 
            tab[j] = tab[j-1]
            j = ... 
        tab[j] = ... 

# Correction
        
# Exercice 1
        
def gb_vers_entier(tab):
    '''
    Renvoie l'entier correspondant à la liste de chiffres tab en binaires big-endian
    '''
    n = 0
    for i in range(len(tab)):
        n = n + tab[i] * 2**(len(tab) - i - 1)
    return n

# Exemple

print("Exercice 1 : Exemple")

print(gb_vers_entier([])) # 0

print(gb_vers_entier([True])) # 1

print(gb_vers_entier([True, False, True, False, False, True, True])) # 83

print(gb_vers_entier([True, False, False, False, False, False, True, False])) # 130

# Exercice 2

def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i] 
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = i
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion

# Exemple

tab = [98, 12, 104, 23, 131, 9]
tri_insertion(tab)
print(tab) # [9, 12, 23, 98, 104, 131]