# Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

a = input('Enter the first number: \n')
b = input('Enter the second number: \n')
if a > b:
    print(f'The first number({a}) is greater than the second number({b})')
elif a < b:
    print(f'The first number({a}) is less than the second number({b})')
else:
    print(f'The first number({a}) is equal to the second number({b})')