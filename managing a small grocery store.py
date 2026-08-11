
fruits = ["apple","orange", "kiwi" ]
fruits.append("Mango")
print(fruits)
vegetables = ["tomato","carrot", "cabbage" ]
vegetables.insert(2, "cucumber")
print(vegetables)
beverages = ["tea","coffee", "blacktea" ]
#del beverages[2]
beverages.remove('blacktea')
print(beverages)
inventory= fruits+vegetables+beverages
print(inventory)
print(fruits[0:2])
print(vegetables[-1:])
fruitlength=[len(item)for item in fruits]
print(fruitlength)
if "Water" in beverages:
    print("Yes, 'water' is in the beverages list")
else:
    print("No,'water' is not in the beverages list")
    fruitsitemsss=(fruits[0],vegetables[0],beverages[0])
    print(fruitsitemsss)