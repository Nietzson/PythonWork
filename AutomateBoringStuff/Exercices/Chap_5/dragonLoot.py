from inventory import displayInventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
theInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)
    return inventory

theInventory = addToInventory(theInventory, dragonLoot)
displayInventory(theInventory)

