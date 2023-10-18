"""
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
"""

sides = [int(a) for a in input('Enter the sides of triangle separated with coma : \n').split(',')]
if sides[0] == sides[1] == sides[2]:
    print('Eq')
elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
    print('Iso')
else:
    print('Scalene')
