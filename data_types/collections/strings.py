
# Python offers a wide variety of functions for string manipulation
# A string is a homogeneous inmutable sequence of Unicode characters.

name = "Angela Merkel"
first_name, surname = name.split(" ")
age = str(65)
tickets = "1 2 3 4 5 6"

country = "mexico".capitalize()
print(country) # -> "Mexico"

# The built-in function converts an integer Unicode codepoint to a 
# single character string.
greetings = chr(104) + chr(105) + "!"
print(greetings) # -> hi!

# The built-in function ord() converts a single character to its integer
# Unicode codepoint.

print(ord("A"), ord("a"))

# ascii() replaces non-ASCII characters with escape sequences.
ascii_string = "H¶llo"
print(ascii(ascii_string))

message = "hi/"
print(message*8, len(message)) # -> hi/hi/hi/hi/hi/hi/hi/hi/ 3

SECRET_KEY = "aerg681erg1weg51v9eg31g6w1av5ew891qw64fzx"
# String to bytes
encoded_key = SECRET_KEY.encode()
# Bytes to string
decoded_key = encoded_key.decode()


# repr: produces an unambiguous string representation of
# an object. Used when:
# Exactness is more important than human-friendliness,
# suited for debugging,
# includes identifying information,
# generally best for logging
def get_sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result
get_sum.__repr__ = 'get_sum(*args)'


class Truck(object):

    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def __repr__(self):
        return f"Truck(width={self.width}, length={self.length})"
minivan = Truck(2, 9)

truck_collections = [Truck(5,i) for i in range(6, 11)]

# repr() is for developers
# The result of repr() should generally contain more information
# than the result of str()
# As a rule, you should ALWAYS WRITE a repr() for your classes.
# str() is for clients
# str() produces a readable, human-friendly representation of
# an object.


print("Age: " + age) # -> "Age: 65"
print("Name: {}, Age: {}".format(name, age)) # -> "Name: Angela Merkel, Age: 65"

# Joining with empty strings is better than the '+' operator
same_tickets = " ".join(["1","2","3","4","5","6"])

print("Country of residence: {country}, Continent: {continent}".format(
    country="China", continent="America"
))

name, _, surname = "Mario-Briseño".partition("-")

noisy_name = "12aMario Briseño00"
clean_name = noisy_name.strip("12a0")

# If a class rewrites __repr__ but not __str__, print() will
# use __repr__ instead. But this doesn't happen backwards, 
# __repr__ won't use __str__ as default it not defined. __repr__
# has a default behavior.
print(minivan)
print(get_sum.__repr__)

# repr() is used when showing elements of a collection
print(truck_collections) # -> [[Truck(width=5, length=6), Truck(width=5, length=7) ...]
