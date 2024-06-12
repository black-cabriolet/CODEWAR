def sum_of_multiples(n):
    # If the number is negative, return 0
    if n < 0:
        return 0

    # Initialize the sum
    total_sum = 0

    # Iterate through all numbers below n
    for i in range(n):
        # Check if the number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # Add the number to the total sum
            total_sum += i

    return total_sum


# Example usage:
result = sum_of_multiples(100)
print(result)  # Output should be 2318
