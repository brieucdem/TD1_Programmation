# ========== Global variables

tirage = ["p", "i", "z", "p", "a", "e", "o", "z"]
path = "frenchssaccent.dic"


# ========== Functions


def read_file(path):
    """
    Read file function.
    Reads the file located at the given path and returns a list of words.
    """
    with open(path, 'r') as f:
        liste = []
        for ligne in f:
            mot = ligne.strip()
            if len(mot) <= 8:
                liste.append(mot)
    return liste


def is_not_possible(tirage, mot):
    """
    Check if word is possible function.
    Returns True if the given word can be formed using the given letters,
    otherwise returns False.
    """
    copie_tirage = list(tirage)
    for lettre in mot:
        if lettre in copie_tirage:
            copie_tirage.remove(lettre)
        else:
            return False
    return True


def score(mot):
    """
    Calculate score function.
    Calculates and returns the score of the given word based on Scrabble scoring rules.
    """
    score = 0
    for lettre in mot:
        if lettre in "aeilnorstu":
            score += 1
        elif lettre in "dgm":
            score += 2
        elif lettre in "bcp":
            score += 3
        elif lettre in "fhv":
            score += 4
        elif lettre in "jq":
            score += 8
        elif lettre in "kwxyz":
            score += 10
    return score


def max_score(liste_mots):
    """
    Maximum score function.
    Finds and returns the word with the maximum score from the given list of words.
    """
    score_max = 0
    mot_max = liste_mots[0]
    for mot in liste_mots:
        if score(mot_max) < score(mot):
            mot_max = mot
            score_max = score(mot)
    return mot_max, score_max


# =========== Main


liste_mots = read_file(path)
mots_possible = []
for mot in liste_mots:
    if is_not_possible(tirage, mot):
        mots_possible.append(mot)

if len(mots_possible) == 0:
    print("No words are possible")
else:
    mot_plus_long = mots_possible[0]
    for mot in mots_possible:
        if len(mot) > len(mot_plus_long):
            mot_plus_long = mot
    print(mots_possible)
    print(mot_plus_long)

if len(mots_possible) != 0:
    meilleur_score = score(mots_possible[0])
    for mot in mots_possible:
        if meilleur_score < score(mot):
            meilleur_score = score(mot)
    print(meilleur_score)
