
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


def print_delimeter():
    print("-" * 25)


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


# Default values are allowed in arguments. Do not use collections as
# default values. They are instantiated once and every call of this 
# function does not allocate a new object in the default value. Instead
# use inmutable types as default arguments (str, int, tuple).
def add_five_to_number(number=0) -> int:
    number += 5
    return number

# Do not do this.           |
#                           V    
def get_initialized_list(arg=[]):
    arg.append(5)
    print(arg)


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

# Single asterisk before a variable allows the function to capture
# any number of unnamed arguments as a tuple.
def add_one_to_variable_number_of_arguments(*args):
    return [arg + 1 for arg in args]


# Double asterisks before a variable allows a function to take
# any number of named variables as a dictionary.
def check_config(**kwargs):
    try:
        print(f"Port is: {kwargs['port']}")
        print(f"API status is: {kwargs['status']}")
        print(f"API rate limit is: {kwargs['rate_limit']} r/s")
    except KeyError:
        print("You are lacking one config parameter.")


def get_common_names(*args, **kwargs):
    return [arg for arg in args] + [kwarg for kwarg in kwargs.values()]


print_delimeter()
weekdays1 = get_week_days()
z = 8
a = add_five_to_number(z)
b = add_five_to_number(z)
print(a is b, a == b) # -> True, True

# Even though local variable is named the same as a varaible out 
# of the function scope the functions doesn't change the value
# of the local variable 'number'
print_delimeter()
number = 10
modify_global_variable() # local 'number' = 5
print(number == 10) # -> True

print_delimeter()
print("Is the USA a member of G7? : ", check_g7_countries("USA"))
print("Is Mexico a member of G7? : ", check_g7_countries("MX"))

print_delimeter()
print("Not the behaviour one would expect, unless you don't know Python")
get_initialized_list()
get_initialized_list()
get_initialized_list()

print(add_one_to_variable_number_of_arguments(-1))
print(add_one_to_variable_number_of_arguments(9, 9, 9))
print(add_one_to_variable_number_of_arguments(5, 9, 6, 1, 0))

check_config(port=8000, status="alive", rate_limit=500)

print(get_common_names("fabian", "isaac", "hugo", 
first_person="mario", second_person="yoel"))
print(get_common_names("chuy", first_person="mario", second_person="yoel"))