#MANAGING AN INVENTORY 
#USE A LIST TO MANAGE INVENTORY ITEMS IN A STORE 

#making an inventory 

inventory = ["apple  " , "banana" , "grapes","kiwi","guava","dragonfruit"] 

#add item
inventory.append("strawberries")
#remove item that is out of stock
inventory.remove("apple")
#checking if item is in inventory 
item = "oranges"
if item in inventory:
    print(f"{item} is in stock ")
else:
    print(f"{item} not in stock")

#print the list 
print("Inventory List :")
for item in inventory:
    print(f"-{item}")
