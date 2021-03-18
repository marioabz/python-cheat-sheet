
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

# Operations are implemented in different ways across data types.
print(Decimal(-7) % Decimal(3) == (-7) // 3)
print(Decimal(-7) // Decimal(3) == (-7) // 3)

# The // operator is known in Python as the floor division operator
# however in the decimal data type this same operator truncates
# towards 0.
result1 = (-7) // 3 # -> -3
result2 = Decimal("-7") // Decimal("3") # -> -2

from fractions import Fraction

# The built-in fractions module allows fraction representations
# through 
first_fraction = Fraction(5, 2)
second_fraction = Fraction("3/8")
third_fraction = Fraction(0.1)
fourth_fraction = Fraction(Decimal("0.1"))

print(first_fraction, second_fraction, third_fraction, fourth_fraction)
print(first_fraction * fourth_fraction)

# Complex
# Python ujses the electrical engineering notation for imaginary
# numbers.
complex_number = 3 + 4j
other_complex_number = complex('5j')
another_complex_number = complex(8, -5)

conjugate = complex_number.conjugate() # -> 3-4j

print(other_complex_number * complex_number, another_complex_number) # -> (-20+15j) (8-5j)

# Printing real and imaginary parts of complex number
print(complex_number.real, complex_number.imag) # -> 3.0, 4.0

import cmath

phase = cmath.phase(complex_number)
absolute_value = abs(complex_number)

# From rectangular coordinates to polar coordinates
same_phase, same_absolute_value = cmath.polar(complex_number)

# From polar coordinates to rectangular coordinates
rectangular_coordinates = cmath.rect(same_phase, same_absolute_value)

print(f"Phase is: {phase}, magnitude of vector: {absolute_value}")
print(same_phase, same_absolute_value)
print(rectangular_coordinates)

pi = 3.14159

print(f"Pi is: {round(pi)}")
print(f"Pi is: {round(pi, 4)}")
print(f"Pi is: {round(Decimal(pi), 3)}")
print(f"Pi is: {round(Fraction(5, 7), 1)}")

# Number base conversions
_bin = bin(4)
_oct = oct(9)
_hex = hex(255)
_int = int("abc", 16)

print(_bin, _oct, _hex, _int)

# The built-in module provides a datetime data type to represent
# dates in the form of Gregorian calendar dates.

# datetime data is composite of date and time
import datetime

#            |
# Avoid this v
# from datetime import datetime

today = datetime.date(2020, 3, 17)
_today = datetime.date.today()
date_from_timestamp = datetime.date.fromtimestamp(1560000000)
todays_time = datetime.time(22, 16, 55, 548623)

print(f"Date is: {today}", _today.day, today.weekday(), today.isoweekday(), 
    date_from_timestamp)

# Hour, minute and second of todays time
print(f"Hour is: {todays_time.hour}, Minute: {todays_time.minute}, Second: {todays_time.second}")
# Not portable since this functionality
formated_date = today.strftime("%A %d %B %Y")
print(formated_date, f", ISO Format: {todays_time.isoformat()}")
