
import decimal
from collections.abc import Callable

# LEGB rule: local, enclosing, global and built-in; rule for name lookup
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
    print("-" * 40)


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


class CubicPolynomial(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        def wrapper(*args, **kwargs):
            last_coefficient = args[-1]
            return f"{last_coefficient}x^3 + " + self.f(*args[:-1], **kwargs)
        return wrapper(*args, **kwargs)

@CubicPolynomial
def quadratic_polynomial(*args):
    return f"{args[-1]}x^2 + {args[-2]}x + {args[-3]}"


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

# The reserved word lambda allows to create anonymous functions.
# Lambda functions tend to be used with other functions like map,
# sort, and filter.
get_repetitions_of_letter_a = lambda x: x.count("a")


# Extended actual argument syntax.
def print_and_group_arguments(a, b, *c):
    print(a, b)
    print(c)


# Closures
# A nested function that has access to a free variable from an 
# enclosing function that has finished its execution.
def enclosure():
    a = 10 # <- variable to be remembered
    c = "hola"
    def local_func(b):
        return a + b, c+"1"
    return local_func


# 'global' keyword introduces names from global namespace into the
# local namespace.
building_height = 100
def enclosing():
    building_height = 89
    def local_function():
        global building_height
        building_height = 50
    print(f"Building height is: {building_height}")
    local_function()
    print(f"Building height is: {building_height}")

print(f"Global building_height is: {building_height}")
enclosing()
print(f"Global building_height is: {building_height}")
print_delimeter()


# 'nonlocal' keyword introduces names from enclosing namespace into the
# local namespace.
building_height = 100
def enclosing():
    building_height = 89
    def local_function():
        nonlocal building_height
        building_height = 50
    print(f"Building height is: {building_height}")
    local_function()
    print(f"Building height is: {building_height}")

print(f"Global building_height is: {building_height}")
enclosing()
print(f"Global building_height is: {building_height}")


# 'check_non_negative' is not a decorator. It is a normal function 
# than return a function that works as a decorator
def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    f"Argument {index} must be non-negative"
                )
            return f(*args)
        return wrap
    return validator


# returns 'validator' wich takes 'create_list' as an argument 
# and decorates it.
@check_non_negative(1)
def create_list(value, size):
    return [value] * size


list_of_a = tuple(map(lambda x: x+"a", ("1", "2", "3", "4", "5")))
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

print("aaaaa", get_repetitions_of_letter_a("aaaaa"))
print(list_of_a)

print_and_group_arguments(*[9, 8, 1, 1, 1, 1])

lf = enclosure()
print(lf(7), lf.__closure__)

print_delimeter()
print(quadratic_polynomial(8, 9, 7, 5))

print_delimeter()
print(create_list(8, 8))
