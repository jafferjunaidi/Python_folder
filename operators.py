a=10
b=3

# Arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # Modulus operator 
print(a//b) # Floor division operator instead of giving the exact result, it rounds down to the nearest whole number floor division cuts off the decimal part and gives you the largest whole number less than or equal to the result.
print(a**b) # Exponentiation operator (a raised to the power of b) a is base , b is exponent 10^3 = 10*10*10 = 1000.

# Comparison operators
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b) 
print(a!=b)

# Augmented assignment operator
c = 6
c += 2 # c = c + 2
c -= 4 # c = c - 4
c *= 6 # c = c * 6
c/=3 # c = c / 3
print(c)

# Logical operators
d=20
e=15

print(d>e and d<e) # and operator returns True if both conditions are True
print(d>e or d==e) # or operator returns True if at least one condition is True
print(not (d>e)) # not operator negates the condition, if the condition is True, it returns False

# Identity operators
f=25
g=30
print(f is not g) # is operator checks if both variables point to the same object in memory
print(f != g)

# Membership operators (use in sequence, set, list, string etc) 
fruits=['apple', 'banana', 'cherry']
print('cherry' in fruits) # in operator checks if the value is present in the sequence
print('orange' not in fruits) # not in operator checks if the value is not present in the sequence

num={21, 32, 43, 57, 64}
print(24 in num)

# Bitwise operators
a=78
b=62
print(a^b, bin(a), bin(b)) 
print(a&b, bin(a), bin(b)) 
print(a|b, bin(a), bin(b)) 
print(a<<2, bin(a), bin(b))  # Left shift operator (shifts bits to the left)
print(a>>2, bin(a), bin(b))  # Right shift operator (shifts bits to the right)
print(~a, bin(a))  # Bitwise NOT operator (inverts the bits)
