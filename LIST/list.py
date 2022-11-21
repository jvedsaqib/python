# Lists are used to store multiple items in a single variable.

list1 = ["Item-1", "Item-2", "Item-3"]
print(list1)    # ['Item-1', 'Item-2', 'Item-3']

# list is mutable
list1.append("Item-4")  
print(list1)    # ['Item-1', 'Item-2', 'Item-3', 'Item-4']

list1.pop()
print(list1)    # ['Item-1', 'Item-2', 'Item-3']

list1[2] = 25
print(list1)    # ['Item-1', 'Item-2', 25]
