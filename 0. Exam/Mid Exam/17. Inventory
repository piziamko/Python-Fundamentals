initial_items = input().split(", ")

command = input()
while not command == "Craft!":
    type_e, item = command.split(" - ")
    if type_e == "Collect":
        if item not in initial_items:
            initial_items.append(item)

    elif type_e == "Drop":
        if item in initial_items:
            initial_items.remove(item)
    elif type_e == "Combine Items":
        command = item
        old_item, new_item = command.split(":")
        if old_item in initial_items:
            index = initial_items.index(old_item)
            initial_items.insert(index+1, new_item)

    elif type_e == "Renew":
        if item in initial_items:
            ind = initial_items.index(item)
            initial_items.pop(ind)
            initial_items.append(item)
    command = input()

print(*initial_items, sep=", ")
