
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

# There is whole list about all available exceptions as builltin in Python
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
