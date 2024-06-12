def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Example usage:
num = 7
result = even_or_odd(num)
print(f"{num} is {result}")
