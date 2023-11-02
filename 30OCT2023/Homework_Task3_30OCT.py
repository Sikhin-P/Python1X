# Remove duplicate elements from a list.

def unique_list(my_list):
    temp = set(my_list)
    unique = list(temp)
    return unique


a = [1, 2, 2, 3, 4, 4, 5]
x = unique_list(a)
print(x)