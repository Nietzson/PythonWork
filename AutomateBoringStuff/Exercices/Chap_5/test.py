spam = {'name': 'Zophie', 'age': 7}
"name" in spam.keys()

#Set a new key-value pair in a dictionary:
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
#Encore mieux!
spam.setdefault("cuisine", "jambonade")

