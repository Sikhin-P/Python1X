"""
Palindrome Checker:
Create a function that checks if a given string is a palindrome
(reads the same forwards and backward). 121
"""


def is_palindrome(my_string):
    my_string = my_string.lower()  # To eliminate conflict with case of letters
    rev_string = my_string[::-1]
    if rev_string == my_string:
        return 'String is palindrome'
    return 'String is not palindrome'


result = is_palindrome('Malayalam')
print(result)
