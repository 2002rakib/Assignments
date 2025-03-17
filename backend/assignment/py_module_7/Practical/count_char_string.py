# Creating a string
my_string = "hello world"

# Creating an empty dictionary to store the counts
char_count = {}

# Looping through each character in the string
for char in my_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Printing the character count
print("Character Count:", char_count)
