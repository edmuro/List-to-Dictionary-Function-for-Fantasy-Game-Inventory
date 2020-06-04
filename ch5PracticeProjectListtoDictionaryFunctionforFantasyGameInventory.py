#Imagine that a vanquished dragon's loot is represented as a list of
#strings like this:
#dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
#Write a functio nanmed addToInventory(inventory,addedItems), where
#the inventory parameter is a dictionary representing the player's
#inventory (like in the previous project) and the addedItems parameter
#is a list like dragonLoot. The addToInventory() function should return
#a dictionary that represents the updated inventory. Note that the
#addedItems list can contain multiples of the same item. Your code
#could look something like this:

def addToInventory(inventory,addedItems):
    #Iterate through list of new items, adding new items to previous
    #inventory. Any new items that appear more than once or items
    #that already were in the old inventory will be combined
    for k in addedItems:
        inventory.setdefault(k,0)
        inventory[k] = inventory[k]+1
    return inventory
        
def displayInventory(quantity):
    print("Inventory:")
    item_total=0 #Initialize total item count
    for k,v in quantity.items():
        print(str(v)+' '+k) #Display both item name and quantity
        item_total = item_total + quantity.get(k,0) #Add quantity to total through 'get'ting the item name

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)

#The previous program (with your displayInventory() function from
#the previous project) would output the following:
#Inventory:
#45 gold coin
#1 rope
#1 ruby
#1 dagger
#
#Total number of items: 48
