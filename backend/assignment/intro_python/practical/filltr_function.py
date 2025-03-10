def odd(number):
    return number % 2 != 0  # Returns True for odd numbers

def filter_odds(numbers):
    return list(filter(odd, numbers))  # Filters out even numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_odds(numbers)

print("Original list: numbers",numbers)
print("Filtered list (odd numbers only): ",filtered_numbers)
