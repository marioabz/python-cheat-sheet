
# Lists are used as arrays to store multiple elements. Those elements
# don't have to be of the same data type

family = ["brother", "sister", "father", "mother"]
lost_and_found_box = ["keys", {(0,1): "1 0"}, 9, 10.0, [1, 2, 3]]
tickets = [1, 2, 3, 4, 5]

# Adding tickets to list
tickets.append(7)
tickets.append(8)
tickets.append(9)

# No more tickets in list
tickets.clear()

# Copy values of list
tickets = [1, 2, 3, 4, 5]
not_the_same_tickets = tickets.copy()
# 'tickets' and 'not_the_same_tickets' are equal in value, but
# they are pointing to different objects
print(not_the_same_tickets == tickets, not_the_same_tickets is tickets)

tickets.append(5)

#Count number of appearances of number
print("The number of 5's in list is: ", tickets.count(5))

# Find index of of number in list
print(list(range(0, 10, 2)).index(8)) # -> 4

print([0, 1, 2] + [3, 4, 5]) # -> [0, 1, 2, 3 ,4, 5]

numbers = [0, 0, 0, 0]
# Insertion at a specific index
numbers.insert(0, 1)
print(numbers) # -> [1, 0, 0, 0, 0]

years = [2000, 2001, 2002, 2003, 2004]

# Removes and returns element. Default is index: -1
years.pop()
print("Years :", years) # -> [2000, 2001, 2002, 2003]

three_series = list(range(10, 0, -3))
print(three_series) # -> [9, 6, 3, 0]

# List is sorted from smaller to greater
three_series.sort()
print("Sorted three series is: ", three_series) # -> [0, 3, 6, 9]

# Reverse the actual order of a list
three_series.reverse()
print("Reversed list of multiple of threes: ", three_series) # -> [9, 6, 3, 0]

the_list = [0, 0, 1, 2, 3]

# Removes the first ocurrance of a value
the_list.remove(0)
print(the_list) # -> [0, 1, 2, 3]

