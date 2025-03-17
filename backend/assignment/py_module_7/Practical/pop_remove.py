# Creating a sample list
my_list = [10, 20, 30, 40, 50, 60]

# Removing an element using pop() - Removes element at a specified index
popped_element = my_list.pop(2)  # Removes the element at index 2 (which is 30)
print("List after pop:", my_list)
print("Popped element:", popped_element)

# Removing an element using remove() - Removes the first occurrence of the specified value
my_list.remove(50)  # Removes the first occurrence of 50
print("List after remove:", my_list)
