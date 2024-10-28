# By ToyHugs

# Énoncé

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def codes_parfait(mot):
    """Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene = ""
    code_additionne = ... 
    for c in mot:
        code_concatene = code_concatene + ... 
        code_additionne = code_additionne + ... 
    code_concatene = int(code_concatene)
    mot_est_parfait = ... 
    return code_additionne, code_concatene, mot_est_parfait

# Corrigé

# Exercice 1

def liste_puissances(n, p):
    """Renvoie la liste des p premières puissances de n.
    Fonction récursive."""
    if p <= 1:
        return [n]
    
    tab = liste_puissances(n, p - 1)
    tab.append(tab[-1] * n)
    return tab


def liste_puissances(n, p):
    """Renvoie la liste des p premières puissances de n.
    Même fonction que la précédente mais sans récursivité."""
    tab = [n]
    for i in range(p - 1):
        tab.append(tab[-1] * n)
    return tab


def liste_puissances_borne(a, borne):
    """Renvoie la liste des puissances de a inférieures à la borne."""
    tab = []
    max_puissance = a
    while max_puissance < borne:
        tab.append(max_puissance)
        max_puissance = max_puissance * a
    
    return tab


# Exemples

print("Exercice 1:")

print(liste_puissances(3, 5)) # [3, 9, 27 ,81 ,243]
print(liste_puissances(-2, 4)) # [-2, 4, -8, 16]
print(liste_puissances_borne(2, 16)) # [2, 4, 8]
print(liste_puissances_borne(2, 17)) # [2, 4, 8, 16]
print(liste_puissances_borne(5, 5)) # []


# Exercice 2

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def codes_parfait(mot):
    """Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene = ""
    code_additionne = 0 
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + int(dico[c]) 
    code_concatene = int(code_concatene)
    mot_est_parfait = code_concatene % code_additionne == 0
    return code_additionne, code_concatene, mot_est_parfait

# Exemples

print("Exercice 2:")
print(codes_parfait("PAUL")) # (50, 1612112, False)
print(codes_parfait("ALAIN")) # (37, 1121914, True)