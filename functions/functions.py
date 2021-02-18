
import decimal
from collections.abc import Callable

# A normal function with the arguments with type specified. One can also
# omit the type specification and the function would work the same
# way:
# Example: print_message_with_delimeters(message: str, delimeter: str) == 
# print_message_with_delimeters(message, delimeter)
def print_message_with_delimeters(message: str, delimeter: str):
    print(delimeter*len(message))
    print(message)
    print(delimeter*len(message))


# Function that returns a list
def get_week_days() -> list:
    return [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]


# Default values are allowed in arguments. Do not use collectibles as
# default values. They are instantiated once and every call of this 
# function does not allocate a new object in the default value
def add_five_to_number(number=0) -> int:
    number += 5
    return number


def modify_global_variable():
    number = 5


# Decorators
# Decorators take a function as an argument and modifies it in order to 
# add 'functiontalities'

def function_modifier(func: Callable) -> Callable:
    def wrapper(arg):
        if len(arg) > 3:
            print("Country does not have a valid length")
            return False
        print("Country has valid abbreviation")
        return func(arg)
    return wrapper


@function_modifier
def check_g7_countries(country: str) -> bool:
    countries = ("USA", "DE", "UK", "FR", "JP", "CA", "IL")
    return country in countries


weekdays1 = get_week_days()
z = 8
a = add_five_to_number(z)
b = add_five_to_number(z)
print(a is b, a == b) # -> True, True

# Even though local variable is named the same as a varaible out 
# of the function scope the functions doesn't change the value
# of the local variable 'number'
number = 10
modify_global_variable() # local 'number' = 5
print(number == 10) # -> True

print("Is the USA a member of G7? : ", check_g7_countries("USA"))
print("Is Mexico a member of G7? : ", check_g7_countries("MX"))