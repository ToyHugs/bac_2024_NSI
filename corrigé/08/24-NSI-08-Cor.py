# By ToyHugs

# Énoncé
class Expr:
    """Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérande ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = ... 
        if self.gauche is not None:
            s = '(' + s + ... .infixe() 
        s = s + ... 
        if ... is not None: 
            s = s + ... + ... 
        return s

# Correction
    
# Exercice 1
    
def delta(tab):
    '''Delta Encoding sur une liste de nombres'''
    n = len(tab)
    tab_delta = [tab[0]]

    for i in range(1, n):
        tab_delta.append(tab[i] - tab[i-1])

    return tab_delta

# Exemple

print("Exercice 1 :")

print(delta([1000, 800, 802, 1000, 1003])) # [1000, -200, 2, 198, 3]

print(delta([42])) # [42]


# Exercice 2

class Expr:
    """Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérande ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = ""
        if self.gauche is not None:
            s = '(' + s + self.gauche.infixe()
        s = s + str(self.valeur)
        if self.droite is not None: 
            s = s + self.droite.infixe() + ')'
        return s
    
# Exemple
    
print("Exercice 2 :")

a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
print(a.infixe()) # (1+2)

b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)), '*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))
print(b.infixe()) # ((1+2)*(3+4))

e = Expr(Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None), '+', Expr(None, 7, None))), '-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))
print(e.infixe()) # ((3*(8+7))-(2+1))

