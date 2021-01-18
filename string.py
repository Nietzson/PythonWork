#recopier la string
s = input("Input: ")
print("Output: ", end="")
for i in range(len(s)):
    print(s[i], end="")#i donne ici l'index, une lettre est écrite à c
    #boucle
print()

#Recopier en majuscule
m = input("Before: ")
print("After: ")
for i in range(len(m)):
    print(m[i].upper(), end="")

