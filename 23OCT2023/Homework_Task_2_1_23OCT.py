# Triangle Star pattern
"""
*
**
***
"""


def star_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print('')


star_pattern(5)
