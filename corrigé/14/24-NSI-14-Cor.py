# By ToyHugs

# Énoncé

'''
class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis cœur, carreau et trèfle. """
        ...
        ...
            ...
                ...

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        ...
        ...
'''

# Correction

# Exercice 1

def min_max(tab):
    '''Renvoie le minimum et le maximum d'un tableau'''
    mini = tab[0]
    maxi = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < mini:
            mini = tab[i]
        if tab[i] > maxi:
            maxi = tab[i]
    return {'min': mini, 'max': maxi}

# Exemple

print("Exercice 1 :")

print(min_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1])) # {'min': -2, 'max': 9}
print(min_max([0, 1, 2, 3])) # {'min': 0, 'max': 3}
print(min_max([3])) # {'min': 3, 'max': 3}
print(min_max([1, 3, 2, 1, 3])) # {'min': 1, 'max': 3}
print(min_max([-1, -1, -1, -1, -1])) # {'min': -1, 'max': -1}

# Exercice 2

class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis cœur, carreau et trèfle. """
        self.contenu = []
        for c in range(1, 5):
            for v in range(1, 14):
                self.contenu.append(Carte(c, v))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        assert 0 <= pos < 52, "paramètre pos invalide"
        return self.contenu[pos]
    
# Exemple
    
print("Exercice 2 :")

'''>>> jeu = Paquet_de_cartes()
>>> carte1 = jeu.recuperer_carte(20)
>>> carte1.recuperer_valeur() \
+ " de " + carte1.recuperer_couleur()
"8 de coeur"
>>> carte2 = jeu.recuperer_carte(0)
>>> carte2.recuperer_valeur() \
+ " de " + carte2.recuperer_couleur()
"As de pique"
>>> carte3 = jeu.recuperer_carte(52)
AssertionError : paramètre pos invalide
4 / 4'''

jeu = Paquet_de_cartes()
carte1 = jeu.recuperer_carte(20)
print(carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur()) # 8 de coeur
carte2 = jeu.recuperer_carte(0)
print(carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur()) # As de pique
carte3 = jeu.recuperer_carte(52)
print(carte3) # AssertionError : paramètre pos invalide
