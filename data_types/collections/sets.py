
# Sets is a type of collection that doesn't index its members.
# Sets are unchangeable and do not allow duplicate values.

numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Returns the difference between 2 sets
print(numbers.difference({6, 7, 8, 9})) # -> {0, 1, 2, 3, 4, 5}

# Create copy of a set
numbers_copy = numbers.copy()
print(numbers == numbers_copy, numbers_copy is numbers) # -> True, False

# Removes element of set, if not in set then it does nothing
numbers.discard(9)

# Return the element at which sets insersect each other
other_set = set(list(range(5,15)))
print(numbers.intersection(other_set)) # -> {8, 5, 6, 7}

# Returns True is sets don't insersect, False if sets inserct
print(set((1, 2, 3)).isdisjoint(set((4,)))) # -> True
print(set((1, 2, 3)).isdisjoint(set((3, 4)))) # -> False

# Returns union of 2 sets
print(set(list(range(5))).union(set(list(range(5,10)))))

q = {5, 10, 15}
# Updates a set with the union of another set
q.update({20, 25,})
print(q) # -> {5, 10, 15, 20, 25}
