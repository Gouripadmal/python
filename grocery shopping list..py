items = ["milk", "bread", "eggs"]

def add_item(item):
    items.append(item)

def remove_last_item():
    items.pop()

display_item = lambda item: print("Item:", item)

def count_characters(items):
    if len(items) == 0:
        return 0
    return len(items[0]) + count_characters(items[1:])

add_item("butter")
remove_last_item()

for item in items:
    display_item(item)

print("Total characters:", count_characters(items))