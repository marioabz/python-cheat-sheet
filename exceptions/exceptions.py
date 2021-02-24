
import sys

# Exception handling is a mechanism for stopping 'normal' program flow
# and continue with surrounding context or other code block.

# The 'try - except' block allows you to catch and handle exceptions.
# One main advantage is that one can avoid the disruptions of the
# intended workflow by catching errors.

# print(1/0) # -> ZeroDivisionError
guests_list_status = {"mario": False, "donald": True, "vladimir": True}
# print(guests_list_status["jinpig"]) # -> KeyError

try:
    raise KeyError
except:
    print("Please don't do this. Except blocks should NOT be too general")

# Catching KeyError and providing useful ouput for the user.
try:
    to_invite = "carlos"
    print(guests_list_status[to_invite])
except KeyError:
    print(f"{to_invite} is not in the guests list")

try:
    print(u"\xe9".encode("ascii"))
except UnicodeEncodeError as e:
    print(e)


try:
    print(9[1])
    print({"a": 1} + 52)
    print([1, 2, 3][3])
except (KeyError, TypeError, IndexError) as e:
    print(e)


# There is whole list about all available exceptions as builltins in Python
# An example of them are: Concrete exceptions, OS exceptions, Warnings,
# System Exit, KeyboardInterrupt, GeneratorExit.

# Libraries often offer exceptions to handle the errors that happen when
# using the library. Examples: boto, redis-py, web3.py, etc.

# Custom exceptions
# It is a good practice to create custom exceptions to handle the possible
# errors in one's code. It allows to clarify the possible errors in the code 
# and plan ahead the handling of those errors.

class NotDivisibleByOddNumbers(ValueError):
    pass

binary_set = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
divisor = 5

#raise NotDivisibleByOddNumbers("This is going to be printed and \
#    potentially written in a log file")

try:
    if divisor % 2 == 1 or divisor == 0:
        raise NotDivisibleByOddNumbers
    print(len(binary_set)/divisor)
except NotDivisibleByOddNumbers as e:
    print("You can only divide binary set with an even number")

# DRY: Don't repeat yourself
divisor = 4
try:
    if divisor % 2 == 1 or divisor == 0:
        raise NotDivisibleByOddNumbers
    print(len(binary_set)/divisor)
except NotDivisibleByOddNumbers as e:
    print("You can only divide binary set with an even number")

# Re rasing exceptions is accepted when unpythonic error make their
# way to one's code.

# One should avoid making the beginner's mistake of having multiple
# tight scopes for multiple callings of the same function.
# One try-catch block should work perfectly fine.

try:
    int(b"5")
    int(6)
    int("8.8")
except ValueError as e:
    print("ValueError: Strings representing floats cannot\
    be converted to Integers.", file=sys.stderr)

# Do not guard Against Type Error
# It's usually not worth checking types. This can limit functions 
# unnecessarily.

# Look Before You Leap Vs. It's Easier to Ask for Forgiveness than
# Permission.
# LBYL vs EAFP

# Local vs. Non-local handling
# Error codes require interspersed, local handling.
# Exceptions allow centralized, non-local handling.

# Code clean up
# The 'finally' block of a try-except block allows to excetute
# a block of code wether an exception ocurred or not.

# Transform a list into a string 
list_to_convert = ["1", "2", "3", "5", (8)]
try:
    strin = ''.join(list_to_convert)
except TypeError as e:
    list_to_convert.pop()
    print(f"Something went wrong. Error: {e}")

try:
    strin = ''.join(list_to_convert)
except TypeError as e:
    print(f"Something went wrong. Error: {e}")
finally:
    print("Joining of list was succesful.")

# Errors should never pass silently, unless explicity silenced.
# A function's exceptions form part of its API, they should be 
# documented properly.
# Prefer to use built-in exception types when possible.
