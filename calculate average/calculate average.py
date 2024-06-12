def find_average(numbers):
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)  # Calculate and return the average

# Example usage:
print(find_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(find_average([]))  # Output: 0
