# Write a Python program to multiply all numbers in a list.

def multiply_list(my_list):
    mul = 1
    for li in my_list:
        mul *= li
    return mul


the_list = [3, 3, 5, 6, 2, 6, 23]
print(multiply_list(the_list))