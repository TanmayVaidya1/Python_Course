# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. 
# It returns True if all the items are present, else it returns False.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

