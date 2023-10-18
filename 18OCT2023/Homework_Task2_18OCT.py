# Example using break to exit a loop when i == 51 while printing the values from 1 to 100

for i in range(1,101):
    if i == 51:
        break
    print(i)

# using continue.
for i in range(1,101):
    if i > 50:
        continue
    print(i)