# multiple of 3
"""
VERSION 1
def m_3 (num):
    if num % 3 ==0:
        return true
    else:
        return false
"""

"""
VERSION 2

test = int(input("Enter any number to determine if multiple of 3: "))

# Define the function outside the loop
def m_3(num):
    return num % 3 == 0

for i in range(5):
    test -= 1  # Decrement the value of test
    result = m_3(test)
    if result:
        print(f'{test} is a multiple of 3')
    else:
        print(f'{test} is not a multiple of 3')

"""

# Prompt the user to enter any number
test = int(input("Enter any number to determine if multiple of 3: "))


# Define a function m_3 to check if a number is a multiple of 3
def m_3(num):
    # Return True if num is divisible by 3, otherwise return False
    return num % 3 == 0


# Iterate from the value of test down to 1 (0 is excluded)
for i in range(test, 0, -1):
    # Check if the current number i is a multiple of 3 by calling m_3
    result = m_3(i)

    # If the result is True, print that the number is a multiple of 3
    if result:
        print(f"{i} is a multiple of 3")
    # If the result is False, print that the number is not a multiple of 3
    else:
        print(f"{i} is not a multiple of 3")

        ###### multiples of 5 ######


# Prompt the user to enter any number
# test = int(input("Enter any number to determine if multiple of 5: "))


# Define a function m_5 to check if a number is a multiple of 5
def m_5(num):
    # Return True if num is divisible by 5, otherwise return False
    return num % 5 == 0


# Iterate from the value of test down to 1 (0 is excluded)
for i in range(test, 0, -1):
    # Check if the current number i is a multiple of 5 by calling m_5
    result = m_5(i)

    # If the result is True, print that the number is a multiple of 5
    if result:
        print(f"{i} is a multiple of 5")
    # If the result is False, print that the number is not a multiple of 5
    else:
        print(f"{i} is not a multiple of 5")
