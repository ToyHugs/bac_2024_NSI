# By ToyHugs

# Énoncé
def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[...] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = ... 
        nb_destinataires = ... 

    return nb_destinataires == ... 

# Correction

# Exercice 1

# Mot à trou : 'INFO*MA*IQUE' et 'INFORMATIQUE'

def correspond(mot, mot_a_trous):
    '''Renvoie True si le mot correspond au mot à trous.'''
    # On vérifie que les mots ont la même longueur
    if len(mot) != len(mot_a_trous):
        return False
    
    # On vérifie que les lettres correspondent
    for i in range(len(mot)):

        # On vérifie que la lettre n'est pas un trou et que les lettres correspondent
        if mot_a_trous[i] != '*' and mot_a_trous[i] != mot[i]: 
            return False
        
    return True
        
# Exemple
print("Exercice 1 : Exemple")

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) # True

print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) # False

print(correspond('STOP', 'S*')) # False

print(correspond('AUTO', '*UT*')) # True

# Exercice 2

# plan_a = {'A':'E', 'B':'F', 'C':'D', 'D':'C', 'E':'B', 'F':'A'} # Double Cycle

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] # On récupère le destinataire de A
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire] # On récupère le destinataire du destinataire
        nb_destinataires = nb_destinataires + 1 # On incrémente le nombre de destinataires

    return nb_destinataires == len(plan) # On vérifie si le nombre de destinataires est égal au nombre de personnes

# Exemple
print("Exercice 2 : Exemple")

print(est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})) # False

print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})) # True

print(est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})) # True

print(est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})) # False