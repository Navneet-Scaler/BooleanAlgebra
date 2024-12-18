""" Is Number Positive? """

# Code 1
"""
number = int(input("Enter a number: "))
if number>0:
    print("Number is Positive.")
else:
    print("Number is Negative.")
"""

# Code 2
"""
def is_positive(number):
    return number>=0

number = int(input("Enter a number: "))

if is_positive(number):
    print(f"{number} is positive")
else:
    print(f"{number} is negative")
"""

# Code 3
def is_positive(number):
    return number>=0

def take_number_input():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid Input! Enter a valid integer")

number = take_number_input()

if is_positive(number):
    print(f"{number} is Positive Integer.")
else:
    print(f"{number} is a Negative Integer.")
