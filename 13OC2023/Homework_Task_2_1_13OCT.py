# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
from math import pi

r = int(input('Enter the radius :\n'))
area = pi * r ** 2
print(f'The area = {area}')
