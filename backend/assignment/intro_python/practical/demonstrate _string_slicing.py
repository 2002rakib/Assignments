# Define a string
my_string = "Hello, World!"

# Basic slicing examples
print("Original string:", my_string)

# Slice from index 0 to index 4 (not inclusive)
print("Slicing from index 0 to 4:", my_string[0:5])

# Slice from index 7 to the end of the string
print("Slicing from index 7 to the end:", my_string[7:])

# Slice from the beginning to index 5 
print("Slicing from beginning to index 5:", my_string[:5])

# Slice with a step value of 2 (every second character)
print("Slicing with a step of 2:", my_string[::2])

# Reverse the string using slicing
print("Reversed string:", my_string[::-1])
