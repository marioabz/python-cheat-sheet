
# Python supports different data types to manage numbers:
# Integers, Floats and Complex

age = 47
x = y = z = 5 # Not ilegal
celsius_degrees = -51
topics = int("941")
height = float(1.75)
half_circle_degrees = complex("0-1i")
positive_infinite = float("inf")
negative_infinite = float("-inf")

# Type Conversion
# In addition and substraction integers are coerced to floats and
# the result is also float
a = 100 + 100.0
print(a) # -> 200.0

# Problems with floats
# Accurate representations of floats are not possible. 
# The library 'Decimal' could help here
# 'decimal' allows more precise control of decimals, critical
# in some applications
import decimal

a = 1.1 + 2.2
print(a) # -> 3.3000000000000003
print(decimal.Decimal("1.1") + decimal.Decimal("2.2")) # -> 3.3
