
# Python supports different data types to manage numbers:
# Integers, Floats and Complex

# int() is an unlimited precision signed integer.
age = 47
x = y = z = 5 # Not ilegal
celsius_degrees = -51
topics = int("941")


height = float(1.75)

# float() is a double precision (64-bit) data type.
# Out of the 64 bits needed to represent a float number,
# 1 bit is used for sign, 11 bits are usedto represent the
# exponent, the value to which the fraction is raised, and 
# the next 52 are dedicated to represent the fraction, aka
# the mantissa or significant.
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
# decimal has ocnfigurable (although finite) precision
# default to 28 digits of decimal precision.
from decimal import (
    Decimal,
    getcontext
)

# To avoid inadvertently constructing Decimal objects from floats,
# the signal handling can be modified in the decimal module

#decimal.getcontext().traps[decimal.FloatOperation] = True
#invalid_decimal_value = Decimal(0.22)

# decimal, unlike float, preserves the precision of numbers supplied
# with trailing 0s.

one_zero = Decimal("37.0")
two_zeros = Decimal("0.00800")
print(one_zero, "One traling zeros preserved")
print(two_zeros, "Two trailing zeros preserved")


a = 1.1 + 2.2
print(a) # -> 3.3000000000000003
print(Decimal("1.1") + Decimal("2.2")) # -> 3.3
