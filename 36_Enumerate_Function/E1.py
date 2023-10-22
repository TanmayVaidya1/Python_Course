# Enumerate function in python
# The enumerate function is a built-in function in Python that allows you to loop over a sequence 
# (such as a list, tuple, or string) and get the index and value of each element in the sequence 
# at the same time. Here's a basic example of how it works:

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
    
# Changing the start index
# By default, the enumerate function starts the index at 0, but you can specify a 
# different starting index by passing it as an argument to the enumerate function:

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)