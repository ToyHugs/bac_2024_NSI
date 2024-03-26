# By ToyHugs

# Énoncé

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // ... 
    if ... < x: 
        return chercher(tab, x, ... , ...) 
    elif tab[m] > x:
        return chercher(tab, x, ... , ...) 
    else:
        return ... 

# Correction
    
# Exercice 1
    
def multiplication(a, b):
    '''Renvoie le produit de a par b.'''
    if b == 0:
        return 0
    if b > 0:
        return a + multiplication(a, b - 1)
    else:
        return - multiplication(a, -b)

# Exemple

print("Exercice 1 :")

print(multiplication(3, 5)) # 15
print(multiplication(-4, -8)) # 32
print(multiplication(-2, 6)) # -12
print(multiplication(-2, 0)) # 0

# Exercice 2

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m + 1, j)
    elif tab[m] > x:
        return chercher(tab, x, i, m - 1)
    else:
        return m

# Exemple

print("\nExercice 2 :")

print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10)) # None
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)) # None
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5)) # 4
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5)) # 2


