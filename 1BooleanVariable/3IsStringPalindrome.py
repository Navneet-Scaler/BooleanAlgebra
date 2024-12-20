""" Is String Palindrime ?"""

# Code 1
"""
str = "Arora"
str_reversed = ''.join(reversed(str.lower()))
print(str_reversed)
if(str.lower() == str_reversed):
    print("Yes, Palindrome")
else:
    print("No, Not Palindrome")
"""

# Code 2
"""
def is_palindrome(str):
    return str.lower() == str[::-1].lower()

str = input("Please enter your string: ")
if is_palindrome(str):
    print("Yes, The Given string is Palindrome.")
else: 
    print("No, The given string is not Palindrome.")
"""

# Code 3
def is_palindrome(str):
    str = str.lower()
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

str = input("Enter a string: ")
if(is_palindrome(str)):
    print("yes, Palindrome")
else:
    print("No, Not Palindrome")