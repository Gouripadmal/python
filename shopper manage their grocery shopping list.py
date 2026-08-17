items=["milk", "bread", "eggs"]
def add_item(item):
  
  items.append(item)
  print(items)

#add_item("ggg")




def remove_last_item():
    items.pop()
    
def sample(n):
  return lambda a : a * n

doubler = sample(2)
print(doubler(10))
    print(items)

remove_last_item()