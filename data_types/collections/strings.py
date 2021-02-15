
# Python offers a wide variety of functions for string manipulation
# A string is a homogeneous inmutable sequence of Unicode characters.

name = "Angela Merkel"
first_name, surname = name.split(" ")
age = str(65)
tickets = "1 2 3 4 5 6"

country = "mexico".capitalize()
print(coutry) # -> "Mexico"

greetings = chr(104) + chr(105) + "!"
print(greetings) # -> hi!

message = "hi/"
print(message*8, len(message)) # -> hi/hi/hi/hi/hi/hi/hi/hi/ 3

SECRET_KEY = "aerg681erg1weg51v9eg31g6w1av5ew891qw64fzx"
# String to bytes
encoded_key = SECRET_KEY.encode()
# Bytes to string
decoded_key = encoded_key.decode()

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
