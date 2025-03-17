# Creating a list with multiple data types
mixed_list = [42, "Hello", 3.14, True, None, [1, 2, 3], {"key": "value"}]

# Printing the list
print("Mixed Data Type List:", mixed_list)

# Iterating through the list and printing type of each element
for item in mixed_list:
    print(f"Element: {item}, Type: {type(item)}")
