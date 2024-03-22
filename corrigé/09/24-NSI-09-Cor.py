# By ToyHugs

# Énoncé

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == ...: 
        return ... 
    else:
        return dec_to_bin(...) + ... 

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if ... == '0': 
            return 0
        else:
            return ... 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            ...
        return ... * bin_to_dec(nb_bin[:-1]) + ... 

# Correction
    
# Exercice 1
    
def effectif_notes(notes_eval):
    '''Effectif des notes d'une évaluation'''
    eff = [0] * 11

    for note in notes_eval:
        eff[note] += 1

    return eff

def notes_triees(eff):
    '''Prend en paramètre un tableau d'effectifs et renvoie la liste des notes triées'''
    notes = []

    for i in range(len(eff)):
        for j in range(eff[i]):
            notes.append(i)

    return notes

# Exemple

print("Exercice 1 :")

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
eff = effectif_notes(notes_eval)
print(eff)
print(notes_triees(eff))

# Exercice 2

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin[0] == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit 
    
# Exemple
    
print("Exercice 2 :")

print(dec_to_bin(42)) # 101010

print(bin_to_dec('101010')) # 42

print(bin_to_dec('1010101')) # 85
