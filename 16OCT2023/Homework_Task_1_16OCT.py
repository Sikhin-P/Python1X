"""
Write a program that calculates and displays the letter grade for a given numerical score
 (e.g., A, B, C, D,or F) based on the following grading scale:
input-score - 89

output- B

A: 90-100

B: 80-89

C: 70-79

D: 60-69

F: 0-59
"""

mark = int(input('Enter the mark obtained : \n'))

if mark in range(90, 101):
    print('The Grade obtained : A')
elif mark in range(80, 90):
    print('The Grade obtained is : B')
elif mark in range(70, 80):
    print('The Grade obtained is : C')
elif mark in range(60, 70):
    print('The Grade obtained : D')
elif mark in range(60):
    print('The Grade obtained is : F')
else:
    print('Invalid entry, please enter a value from 0 to 100')
