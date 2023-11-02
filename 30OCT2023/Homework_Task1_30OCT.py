# Find the maximum and minimum elements in a tuple.

def min_and_max(my_tuple):
    mini = my_tuple[0]
    maxi = my_tuple[0]
    for item in my_tuple:
        if mini > item:
            mini = item
        if maxi < item:
            maxi = item
    return mini, maxi


a, b = min_and_max((15, 8, 25, 36, 42, 10))
print(f'Minium : {a} and Maximum : {b}')
