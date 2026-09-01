import random
import math
names = input("Enter the name of invited guests:");
names = [name.strip() for name in names.split(",")]
names = list(set(names))
selected_name = random.choice(names)


reversed_name = selected_name[::-1]


print("Selected name:", reversed_name)


print("Total unique names:", len(names))


square_root = round(math.sqrt(len(names)))
print("Square root of unique names:", square_root)

    
  
   