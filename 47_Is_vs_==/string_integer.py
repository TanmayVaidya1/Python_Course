# One important thing to note is that, in Python, strings and integers are immutable, which means that 
# once they are created, their value cannot be changed. This means that, for strings and integers, 
# is and == will always return the same result:

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True