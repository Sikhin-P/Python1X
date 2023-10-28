# multiplying elements of two lists using map

def multiplier(list_1, list_2):
    mul = list(map(lambda x, y: x * y, list_1, list_2))
    return mul


list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
print(multiplier(list1, list2))
