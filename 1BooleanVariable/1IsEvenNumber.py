""" Is Number Even? """

# Code 1
"""
number = int(input("Enter a number: "))
if number%2==0:
    print("Numebr is Even")
else:
    print("Numebr is odd.")
"""

# Code 2
"""
def is_even(number):
    return number % 2 == 0

number = int(input("Enter a number: "))

if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
"""

# Code 3
"""
def is_even(numebr):
    return number % 2 == 0

# Take input cosidering the error
def take_number_input():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid Input! Enter a valid integer.")

number = take_number_input()

if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
"""














"""
Learnings : 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8.
9.
10. 
"""