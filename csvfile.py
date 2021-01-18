import csv

file = open("phonebook.csv", "a")# a pour "append", donc ajout de données.

name = input("Name: ")
number = input("Number: ")

with writer = csv.writer(file)
#with permet de ferme le fichier une fois le travail fini, évitant donc
#de devoir mettre "file.close()".
#Ouvrir le fichier "file" par le biais du package
                         #csv, avec l'option d'écriture
writer.writerow((name, number))