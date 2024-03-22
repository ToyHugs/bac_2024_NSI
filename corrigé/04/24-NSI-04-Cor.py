# By ToyHugs

# Énoncé
def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre 
    deux points."""
    return (...)**2 + (...)**2 

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se 
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = ... 
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < ...: 
            min_point = ... 
            min_dist = ... 
    return min_point

# Correction

# Exercice 1

def recherche(tab, x):
    """Renvoie l'indice de la dernière occurrence de x dans tab, ou None si x n'est pas dans tab."""

    # On parcourt le tableau en partant de la fin
    for i in range(len(tab) - 1, -1, -1):
        if tab[i] == x:
            return i # On renvoie l'indice de la dernière occurrence de x
        
    return None # Si x n'est pas dans tab, on renvoie None

# Exemple

print("Exercice 1 : Exemple")

print(recherche([5, 3],1)) # None

print(recherche([2,4],2)) # 0

print(recherche([2,3,5,2,4],2)) # 3

# Exercice 2

def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre 
    deux points."""
    # On calcule la distance au carré entre les deux points
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se 
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = distance_carre(tab[0], depart) # On initialise la distance minimale à la distance entre le premier point et le point de départ
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < min_dist: # Si la distance entre le point i et le point de départ est inférieure à la distance minimale
            min_point = tab[i] # On met à jour le point le plus proche
            min_dist = distance_carre(tab[i], depart) # On met à jour la distance minimale
    return min_point

# Exemple

print("Exercice 2 : Exemple")

print(distance_carre((1, 0), (5, 3))) # 25

print(distance_carre((1, 0), (0, 1))) # 2

print(point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)])) # (2, 5)

print(point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)])) # (5, 2)