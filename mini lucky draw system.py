import random
import math
names = input("Enter the name of customers:");
names = [name.strip() for name in names.split(",")]
names = list(set(names))
random.shuffle(names)
if len(names) >= 2:
   winners = random.sample(names, 2)
   winner1 = winners[0][::-1]
   winner2 = winners[1][::-1]
   print("\nWinners:")
   print(winner1)
   print(winner2)

    
   print("Total unique participants:", len(names))

    
   result = round(math.sqrt(len(names)))
   print("Square root of participants:", result)

else:
     print("Please enter at least 2 unique names.")