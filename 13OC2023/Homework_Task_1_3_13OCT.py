# What does the ^ operator do in Python, and in what context is it commonly used?

a = 10 ^ 9
print(a)

"""
Results bit 1,if any of the operand bit is 1 but not both, otherwise 
results bit 0.

1. Integer 10 converts to 1010 binary form 
2. Integer 9 converts to 1001 binary form
3. then compares each bits of both operands
4. then the result 0011 coverts to decimal which is 3

"""