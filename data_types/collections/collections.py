
# Collections can be nested and can have multiple inputs.

my_list = [f"{x}/{y}" for x in range(5) for y in range(5,11)]
print(my_list)

list_of_lists = [[f"{i}{chr(x)}{i}" for x in range(97, 102)] for i in range(3)]
print(list_of_lists)
