# map
# The map function applies a function to each element in a sequence and 
# returns a new sequence containing the transformed elements. The map function has the 
# following syntax:

# map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. 
# The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the map function:

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))