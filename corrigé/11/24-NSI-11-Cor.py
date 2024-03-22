# By ToyHugs

# Énoncé
'''
class Noeud:
    def __init__(self, etiquette):
        \'''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.\'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        \'''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.\'''
        if cle < self.etiquette:
            if self.gauche != None:
                ...
            else:
                self.gauche = ... 
        else:
            ...
                ...
            else:
                ... = Noeud(cle) 
'''

# Correction

# Exercice 1

def nombre_de_mots(phrase):
    '''Renvoie le nombre de mots dans une phrase'''
    nb_espace = 0
    for lettre in phrase:
        if lettre == ' ':
            nb_espace += 1
    
    if phrase[-1] == '.': # Si la phrase se termine par un point
        nb_espace += 1
    
    return nb_espace # Si la phrase se termine par '!' ou '?', on a un espace supplémentaire entre le dernier mot et le point, donc on ne rajoute pas 1

# Exemples

print("Exercice 1 :")
print(nombre_de_mots('Cet exercice est simple.')) # 4
print(nombre_de_mots('Le point d exclamation est séparé !')) # 6
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?')) # 10
print(nombre_de_mots('Fin.')) # 1

# Exercice 2

class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle) # On appelle la méthode récursivement
            else:
                self.gauche = Noeud(cle) # On crée un nouveau noeud
        else:
            if self.droit != None: # On vérifie si le noeud droit n'est pas vide
                self.droit.inserer(cle) # On appelle la méthode récursivement
            else:
                self.droit = Noeud(cle)  # On crée un nouveau noeud

# Exemples

print("Exercice 2 :")

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

print(arbre.gauche.etiquette) # 3
print(arbre.droit.etiquette) # 9
print(arbre.gauche.gauche.etiquette) # 1
print(arbre.gauche.droit.etiquette) # 6