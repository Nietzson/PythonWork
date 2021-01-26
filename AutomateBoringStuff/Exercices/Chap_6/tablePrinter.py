#Imprimer un tableu correctement justifié
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    listNum= len(table)
    itemList= len(table[0])
    colWidths = [0] * len(table)
    for i in table:
        for j in i:
            if colWidths[table.index(i)] < len(j):
                colWidths[table.index(i)] = len(j)
    print(colWidths)
    for col in range(itemList):
        for list in range(listNum):
            print(table[list][col].rjust(colWidths[list]), end = " ")
        print(" ")

printTable(tableData)

