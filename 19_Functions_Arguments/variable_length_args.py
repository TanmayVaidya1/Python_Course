# There are two ways to achieve this:

# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of tuple.

# def name(*name):
#     print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan", "Barnes")


# Keyword Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

