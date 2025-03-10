class MyIterator:
    def __init__(self, data):
        self.data = data  # List of integers
        self.index = 0     # Initialize the index for iteration

    def __iter__(self):
        return self  # The iterator object itself is returned

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]  # Get the current item
            self.index += 1  # Move to the next item
            return result
        else:
            raise StopIteration  # Stop iteration when the list is exhausted

# Example usage
numbers = [10, 20, 30, 40, 50]
iterator = MyIterator(numbers)

# Iterate over the list using the custom iterator
for num in iterator:
    print(num)
