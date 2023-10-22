# We can use remove() and discard() methods to remove items form list.

# Example :
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)


# The main difference between remove and discard is that, 
# if we try to delete an item which is not present in set, then remove() raises an error, 
# whereas discard() does not raise any error.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)