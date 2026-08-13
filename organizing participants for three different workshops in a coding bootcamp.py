webdevelopment = ["hari","jai", "Ram" ]
#fruits.append("Mango")
#print(fruits)
Datascience = ["Manu","Sunu", "Binu" ]
#vegetables.insert(2, "cucumber")
#print(vegetables)
UI/UX_design = ["Jigu","Janu", "bikku" ]
#del beverages[2]
#beverages.remove('blacktea')
#print(beverages)
all_participants= webdevelopment+Datascience+UI/UX_design
print(all_participants)
webdevelopment.append("haara")
Datascience.insert(2, "shraddha")
UI/UX_design.remove('bikku')
new_Datascience = Datascience.copy()
print(new_Datascience)

print(webdevelopment[0:2])




print(vegetables[-1:])
fruitlength=[len(item)for item in fruits]
print(fruitlength)
if "Water" in beverages:
    print("Yes, 'water' is in the beverages list")
else:
    print("No,'water' is not in the beverages list")
    fruitsitemsss=(fruits[0],vegetables[0],beverages[0])
    print(fruitsitemsss)
    inventory= fruits+vegetables+beverages
print(inventory)