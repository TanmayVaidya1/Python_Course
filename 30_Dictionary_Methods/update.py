# update()
# The update() method updates the value of the key provided to it 
# if the item already exists in the dictionary, else it creates a new key-value pair.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)