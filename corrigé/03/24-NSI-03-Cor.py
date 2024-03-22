# By ToyHugs

# Énoncé
class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch 
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == ...: 
            p.empiler(c)
        elif c == ...: 
            if p.est_vide():
                ...
            else:
                ...
    return ... 

# Correction

# Exercice 1

def maximum_tableau(tab):
    """Renvoie le maximum d'un tableau tab"""
    max = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
    return max

# Exemple
print("Exercice 1 : Exemple")

print(maximum_tableau([98, 12, 104, 23, 131, 9])) # 131

print(maximum_tableau([-27, 24, -3, 15])) # 24

# Exercice 2

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch 
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == "(": # On empile les parenthèses ouvrantes
            p.empiler(c)
        elif c == ")":  # On dépile les parenthèses fermantes
            if p.est_vide():
                return False # Si la pile est vide, la chaîne n'est pas bien parenthésée
            else:
                p.depiler() # Sinon, on dépile
    return p.est_vide() # Si la pile est vide, la chaîne est bien parenthésée, sinon non

# Exemple
print("Exercice 2 : Exemple")

print(bon_parenthesage("((()())(()))")) # True

print(bon_parenthesage("())(()")) # False

print(bon_parenthesage("(())(()")) # False