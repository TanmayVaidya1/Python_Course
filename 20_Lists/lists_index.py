# List Index
# Each item/element in a list has its own unique index. 
# This index can be used to access any particular item from the list. 
# The first item has index [0], second item has index [1], third item has index [2] and so on.

# Example:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

# Positive Indexing:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# Negative Indexing:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#   [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

# Check whether an item in present in the list?

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Yellow" in colors:
#     print("Yellow is present.")
# else:
#     print("Yellow is absent.")

# Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end 
# and if you want to skip elements in between the range.

# Syntax:
# listName[start : end : jumpIndex]
# Note: jump Index is optional. We will see this in later examples.

#Example: printing elements within a particular range:
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

#Example: printing all element from a given index till the end
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[4:])	#using positive indexes
# print(animals[-4:])	#using negative indexes

#Example: printing all elements from start to a given index
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[:6])	#using positive indexes
# print(animals[:-3])	#using negative indexes

#Example: printing all elements from start to a given index
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[:6])	#using positive indexes
# print(animals[:-3])	#using negative indexes

#Example: printing every 3rd consecutive value withing a given range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
