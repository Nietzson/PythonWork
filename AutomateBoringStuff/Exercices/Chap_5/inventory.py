import pprint
theInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    totItems = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        totItems += v
    print("Total number of items:" + str(totItems))

displayInventory(theInventory)

######################################DRAGON LOOT#########################################
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory:
            inventory[i] = 1
        else:
            inventory[i] += 1
    return inventory

theInventory = addToInventory(inv, dragonLoot)
displayInventory(theInventory)



