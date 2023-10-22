'''
A class is a blueprint or a template for creating objects, 
providing initial values for state (member variables or attributes), 
and implementations of behavior (member functions or methods). 
The user-defined objects are created using the class keyword.
'''
class Details:
    name = "Rohan"
    age = 20
    
'''
Object is the instance of the class used to access the properties 
of the class Now lets create an object of the class.
'''
obj1 = Details()

print(obj1.name)
print(obj1.age)