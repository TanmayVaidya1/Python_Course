# del:
# we can also use the del keyword to remove a dictionary item.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# If key is not provided, then the del keyword will delete the dictionary entirely.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)