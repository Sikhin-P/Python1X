# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.

def sum_of_digits(num):
    temp = str(num)
    my_sum = 0
    for t in temp:
        my_sum += int(t)
    return my_sum


sum_of = sum_of_digits(123456789)
print(sum_of)
