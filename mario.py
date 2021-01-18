#4cases "?""
for i in range(4):
    print("?",end="")
print()

#colonne de 3=trois briques
print("#\n" *3, end="")

#un carré de avec une texture de briques
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()