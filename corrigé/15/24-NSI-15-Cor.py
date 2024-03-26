# By ToyHugs

# Énoncé

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return ... 
    bin_a = ... 
    while ... : 
        bin_a = ... + bin_a 
        a = ... 
    return bin_a

# Correction

# Exercice 1

def moyenne(tab):
    '''Renvoie la moyenne des éléments d'un tableau'''
    somme = 0
    for i in range(len(tab)):
        somme += tab[i]
    return somme / len(tab)

# Exemple

print("Exercice 1 :")
tab = [1, 2, 3, 4, 5]
print(f"La moyenne de {tab} est {moyenne(tab)}.")
# La moyenne de [1, 2, 3, 4, 5] est 3.0.

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


a = 83
print(f"Le nombre {a} en binaire est {binaire(a)}.")
# Le nombre 83 en binaire est 1010011.

a = 6
print(f"Le nombre {a} en binaire est {binaire(a)}.")
# Le nombre 6 en binaire est 110.

a = 127
print(f"Le nombre {a} en binaire est {binaire(a)}.")
# Le nombre 127 en binaire est 1111111.

a = 0
print(f"Le nombre {a} en binaire est {binaire(a)}.")
# Le nombre 0 en binaire est 0.