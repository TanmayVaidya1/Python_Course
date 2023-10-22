'''
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar 
to both the sets. The symmetric_difference() method returns a new set whereas
symmetric_difference_update() method updates into the existing set from another set.
'''

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)