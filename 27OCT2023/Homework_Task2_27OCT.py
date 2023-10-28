# Write a Python program to find the smallest number in a list.

def smallest(my_list):
    small = my_list[0]
    for li in my_list:
        if li < small:
            small = li
    return small


the_list = [56, 45, 232, 532, 2342, 98, 35, 76]
print(smallest(the_list))
