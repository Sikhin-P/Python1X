# Explain the difference between the = operator and the == operator in Python.
"""
The = is called as assignment operator which is used to assign a value to a variable.
"""
a = 10
# here the integer value 10 is assigned to the variable 'a'

a += 2
# Add and Assign: Add right side operand with left side operand and then assign to left operand

a *= 3
# Multiply AND: Multiply right operand with left operand and then assign to left operand

print(a)

"""
Like this we can other combinations such as

-= 
Subtract AND: Subtract right operand from left operand and then assign to left operand: True if both operands are equal

/=
Divide AND: Divide left operand with right operand and then assign to left operand

%=
Modulus AND: Takes modulus using left and right operands and assign result to left operand

//=
Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand

**=
Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand

&=
Performs Bitwise AND on operands and assign value to left operand

|= 
Performs Bitwise OR on operands and assign value to left operand	

^=
Performs Bitwise xOR on operands and assign value to left operand

>>=
Performs Bitwise right shift on operands and assign value to left operand

<<=
Performs Bitwise left shift on operands and assign value to left operand
"""