import random

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

# Generate a random integer between 1 and 100 (inclusive)
random_integer = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_integer}")

# Generate a random number from a given list
sample_list = [10, 20, 30, 40, 50]
random_choice = random.choice(sample_list)
print(f"Random choice from the list: {random_choice}")
