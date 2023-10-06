# 1.Print the Name of the user by taking it from the input command.

name = input('Enter your name: ')
print(name)

# 2. Take first name and last name of user and print with sep. = "-" and end with /t.

first_name = input('Enter the first name:')
last_name = input('Enter the last name:')
print(first_name, last_name, sep='-', end='\t')

# 3.Take a user input as name and say with message You are welcome. "<Pramod>" to the Python Class.

name = input('Enter your name:')
print(f'Hello {name} welcome to the Python Class.')
