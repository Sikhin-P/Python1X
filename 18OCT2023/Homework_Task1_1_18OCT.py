# Fibonacci series
"""
The Fibonacci Sequence is the series of numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers before it
"""

n = int(input('Enter the limit :'))
if n < 2:
    print('Enter a limit more than 1')
else:
    series = [0,1]
    for i in range(n-2):
        series.append(series[-1] + series[-2])
    print(*series, sep=', ')

