
# Dictionary is a collection that stores values in a key-value fashion
# Dictionaries are changeable and don't allow duplicates

person = {
    "age": 67,
    "name": "Jinpig",
    "last_name": "Xi",
    "ocupation": "President",
    "country_of_origin": "China",
}

# Accesing the 'age' key of dict 'person'
print(person["age"])

# Updating the value of key 'country_of_origin'
person["country_of_origin"] = "Taiwan"

# Create a copy of person but they are no the same object
copycat = person.copy()
print(person == copycat, person is copycat) # -> True, False

keys = "age", "name", "last_name", "ocupation", "country_of_origin"
#Create a dict with iterable as keys
person_to_set = dict.fromkeys(keys, None)
print(person_to_set)

# Returns the keys and values in a list of tuples
print(person.items()) 
# -> dict_items([('age', 67), ('name', 'Jinpig'), 
# ('last_name', 'Xi'), ('ocupation', 'President'), 
# ('country_of_origin', 'China')])

# Returns a list of keys of a dict
print(person.keys()) # -> dict_keys(['age', 'name', 'last_name', 'ocupation', 'country_of_origin'])

# Returns a list of values of a dict
print(person.values()) # -> dict_values([67, 'Jinpig', 'Xi', 'President', 'China'])

# Returns the value asociated with the key
print(person.pop("ocupation")) # -> 'President'

# Returns a default value if key doesn't exist in dict
print(person.pop("countryyy", "-")) # -> '-'
 