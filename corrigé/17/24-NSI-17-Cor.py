# By ToyHugs

# Énoncé

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ... 
    while ...: 
        bin_a = ... + bin_a 
        a = ... 
    return bin_a

# Correction

# Exercice 1

def nb_repetitions(elt, tab):
    '''Renvoie le nombre de fois où l'élément elt apparaît dans le tableau tab.'''
    nb = 0
    for i in range(len(tab)):
        if tab[i] == elt:
            nb += 1
    return nb

# Exemple

print("Exercice 1 :")

print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5])) # 3
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R'])) # 2
print(nb_repetitions(12, [1, 3, 7, 21, 36, 44])) # 0


# Exercice 2

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2 
    return bin_a

# Exemple

print("\nExercice 2 :")

print(binaire(0)) # '0'
print(binaire(2)) # '10'
print(binaire(77)) # '1001101'