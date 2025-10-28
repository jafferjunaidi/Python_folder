import math # Importing the math module
num1=43.7
print(math.ceil(num1)) # Using the ceil function to round up to the nearest integer

num2=57
print(math.floor(num2)) # Using the floor function to round down to the nearest integer

num3 = -66
print(math.fabs(num3)) # fabs() stands for floating-point absolute value. It returns the positive version of a number, whether it's negative or not.

print(math.sqrt(125)) # Using the sqrt function to calculate the square root of a number

marks=[45.68, 67, 89, 23.5, 56, 78, 67.46]
print(math.fsum(marks)) # fsum() function calculates the precise floating-point sum of all the values in the list.
                        # It is more accurate than the regular sum() function, especially for large lists of floating-point numbers.


