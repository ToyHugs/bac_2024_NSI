# By ToyHugs

# Énoncé

"""def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x ... : 
        acc.append(x)
        for y in ...: 
            parcours(adj, ...) """

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, ...) 
    return acc

# Corrigé

# Exercice 1

def recherche_motif(motif, texte):
    tab_motif = []

    for i in range(len(texte)): # Parcours du texte

        parcours_reussi = True

        for j in range(len(motif)): # Parcours du motif pour chaque caractère du texte

            if (i + j) >= len(texte): # Si le texte est trop long
                parcours_reussi = False
                break

            if (texte[i + j] != motif[j]): # Si le motif est différent
                parcours_reussi = False
                break

        if parcours_reussi:
            tab_motif.append(i)

    return tab_motif

# Exemples






