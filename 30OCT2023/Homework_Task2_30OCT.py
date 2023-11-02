# Find the intersection and union of two sets.

def inter_and_uni(set1, set2):
    inter = set1.intersection(set2)
    uni = set1.union(set2)
    return inter, uni


a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
x, y = inter_and_uni(a, b)
print(f'Intersection : {x}')
print(f'Union : {y}')
