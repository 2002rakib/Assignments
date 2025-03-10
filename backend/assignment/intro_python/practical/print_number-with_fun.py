def even_numbers():
    num = 2
    for _ in range(10):
        yield num
        num += 2

# Example usage
for even_number in even_numbers():
    print(even_number)
