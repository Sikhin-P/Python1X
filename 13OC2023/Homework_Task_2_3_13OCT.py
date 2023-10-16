# Use the ternary operator to find the maximum of three numbers entered by the user.


a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))

maximum = (a if a > b and a > c else b if b > c else c)
print(f'The maximum = {maximum}')
