import os
item = input("Enter the name of new item: ")
if not os.path.exists("item.txt"):
  with open("item.txt", "w") as file:
      file.write(item +"\n")
else:
  with open ("item.txt", "a") as file:
            file.write(item )  

print("\n Item in the shop:")
with open("item.txt", "r") as file:
    for line in file:
        print(line.strip())