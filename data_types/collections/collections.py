
# Collections can be nested and can have multiple inputs.

my_list = [f"{x}/{y}" for x in range(5) for y in range(5,11)]
print(my_list)

list_of_lists = [[f"{i}{chr(x)}{i}" for x in range(97, 102)] for i in range(3)]
print(list_of_lists)

# map() applies a function to every element in a sequence,
# producing a new sequence.
# map() has a lazy evaluation: it produces values as they
# are needed
ages = [24, 25, 26, 50, 21, 63, 78, 41, 89]
young_people = map(lambda x: 20 <= x <= 30, ages)
print(list(young_people))

# map() can also have multiple input sequences
# sequences have to have the same length among them
girls = [chr(i) for i in range(97, 102)]
boys = [chr(i) for i in range(102, 107)]
pairs = list(map(lambda x,y: f"{x}+{y}", girls, boys))
print(pairs)
