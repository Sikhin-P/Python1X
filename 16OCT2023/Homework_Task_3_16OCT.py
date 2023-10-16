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

angles = [int(a) for a in input('Enter the angles of triangle separated with coma : \n').split(',')]
if angles[0] == angles[1] == angles[2]:
    print('Eq')
elif angles[0] == angles[1] or angles[0] == angles[2] or angles[1] == angles[2]:
    print('Iso')
else:
    print('Scalene')
