from functools import reduce

# Define a normal function for multiplication
def multiply(x, y):
    return x * y

def product_of_list(numbers):
    if not numbers:
        return None  # Handle empty list case
    return reduce(multiply, numbers)

# Example usages
examples = [
    [2, 3, 4, 5],        
    [1, 2, 3],           
       
]

for nums in examples:
    result = product_of_list(nums)
    print(f"Product of {nums} is: {result}")
