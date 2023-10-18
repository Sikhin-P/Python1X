# Factorial
"""
The Factorial of a whole number 'n' is defined as the product of that number with every whole number
less than or equal to 'n' till 1. For example, the factorial of 4 is 4 × 3 × 2 × 1, which is
equal to 24. It is represented using the symbol '!' So, 24 is the value of 4!.
"""


n = int(input('Enter the number :'))
num = n
fact = 1
if n >= 0:
    for n in range(n, 0, -1):
        fact *= n
    print(f'Factorial of {num} is : {fact}')
else:
    print('Invalid Entry')