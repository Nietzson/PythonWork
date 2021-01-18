words = set()

def check(word):
    if word.lower() in words: #lower est une fonction qui permet
    #passer outre les lettres capitales
    #éventuelles
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, "r")  # "r" pour "read mode"
    for line in file!
        words.add(line.rstrip("\n")) # rstrip pour enlever les caracteres
        #\n de retour à la ligne à la fin de chaque mot du dictionnaire.
    file.close()
    return True


def size():
    return len(words)

def unload():#libérer la mémoire, OSEF
    return True
