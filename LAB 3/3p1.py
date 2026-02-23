lst = [10, 20, 30, 40]

# Insert
lst.insert(2, 25)
print(lst)

# Delete
lst.remove(30)
print(lst)

# Search
element = 40
if element in lst:
    print("Element found")
else:
    print("Element not found")
