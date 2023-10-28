# Write a Python program to find the largest number in a list.

# by comparing each number in a list
def largest(my_list):
    large = my_list[0]
    for li in my_list:
        if li > large:
            large = li
    return large


# by using inbuilt sorted function
def largest_by_sorting(my_list):
    temp_list = sorted(my_list)
    return temp_list[-1]


the_list = [1, 3, 5, 3, 56, 23, 43, 98, 45]
largest_num = largest(the_list)
print(largest_num)
largest_num = largest_by_sorting(the_list)
print(largest_num)