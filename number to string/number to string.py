# def number_to_string(num):
#     num = string(num)
#     return num
# x = input("enter x")
# y = number_to_string(x)
# print(type(y), "this is the data type of x ")

# try:
#     x = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a valid number!")

# def number_to_string(num):
#     num = str(num)  # Use str instead of string
#     return num
#
# x = input("Enter x: ")  # Input is already a string
# y = number_to_string(x)
# print(type(y), "this is the data type of y")  # Print type of y and message


def number_to_string(num):
    num = str(num)
    return num


x = input("Enter x: ")

"""
this makes sure that the input is an integer.if not the error message is displayed and program exited
"""
try:
    x = int(x)  # Convert input to an integer
except ValueError:
    print("Please enter a valid number")
    exit()

y = number_to_string(x)
print(type(y), "this is the data type of y")
