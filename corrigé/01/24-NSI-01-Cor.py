# By ToyHugs

# Énoncé
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = ... 
    tab[i] = ... 
    tab[j] = ... 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(...): 
        imin = ... 
        for i in range(..., N): 
            if tab[i] < ...: 
                imin = i
        echange(tab, ..., ...) 

# Correction
        
# Exercice 1
        
# Arbre sous forme a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}
        
def taille(tab, lettre):
    '''Renvoie la taille de l'arbre binaire de recherche tab, dont la racine est lettre.'''

    # Cas d'un arbre sans fils
    if tab[lettre][0] == '' and tab[lettre][1] == '':
        return 1
    
    # Cas d'un arbre avec un seul fils sur le premier index
    elif tab[lettre][0] == '':
        return 1 + taille(tab, tab[lettre][1])

    # Cas d'un arbre avec un seul fils sur le deuxième index
    elif tab[lettre][1] == '':
        return 1 + taille(tab, tab[lettre][0])
    
    # Cas d'un arbre avec deux fils
    else:
        return 1 + taille(tab, tab[lettre][0]) + taille(tab, tab[lettre][1])
    
# Exemple
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

print("Exercice 1 : Exemple")

print("Taille pour F : ", taille(a, 'F')) # 9
print("Taille pour B : ", taille(a, 'B')) # 5
print("Taille pour I : ", taille(a, 'I')) # 2

# Exercice 2
    
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N-1): # On ne va pas jusqu'à N car le dernier élément est déjà trié
        imin = k # On initialise l'indice du minimum
        for i in range(k+1, N): # On met k+1 pour ne pas comparer avec les éléments déjà triés. Pour information k aurait aussi pu fonctionner, mais c'est moins efficace
            if tab[i] < tab[imin]: # On écrit tab[imin] et non tab[k] car on peut avoir k > imin
                imin = i
        echange(tab, k, imin) # On échange le minimum avec l'élément d'indice k

# Exemple
tab = [41, 55, 21, 18, 12, 6, 25]

print("Exercice 2 : Exemple")

tri_selection(tab)
print(tab) # [6, 12, 18, 21, 25, 41, 55]
