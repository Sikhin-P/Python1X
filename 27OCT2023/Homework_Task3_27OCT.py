# Write a Python program to sum all numbers in a list.

# Using inbuilt sum function
def sum_of_list(my_list):
    total = sum(my_list)
    return total


# Using a loop to add each numbers in a list
def sum_of_list2(my_list):
    total = 0
    for li in my_list:
        total += li
    return total


the_list = [1, 343, 23, 54, 89, 9, 98]
print(sum_of_list(the_list))
print(sum_of_list2(the_list))