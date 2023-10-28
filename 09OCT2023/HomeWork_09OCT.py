# print unique numbers from user's input

# Taking numbers from users as a list
# converting entered string to number, for loop used here to split each entry and add to the list.
numbers = [int(n) for n in input("Enter the numbers separated with comma\n").split(",")]

# converting list to a set to eliminate duplicate numbers.
unique = set(numbers)

print(*unique)

# Sample Input : 1,2,3,4,5,11,22,16,10,0,1,4,5
# Expected Result {0, 1, 2, 3, 4, 5, 10, 11, 16, 22}
