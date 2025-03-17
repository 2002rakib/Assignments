# Lambda function to square a number
square = lambda x: x * x

# Calling the lambda function
print(square(5))

#_________________________________________________________________________

#Program to create a lambda function with two expressions:

# Lambda function with two expressions (using a tuple)
add_and_square = lambda x, y: (x + y, (x + y) ** 2)

# Calling the lambda function
result = add_and_square(3, 4)
print("Sum:", result[0])
print("Square of Sum:", result[1])
