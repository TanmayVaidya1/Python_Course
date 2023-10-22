# Raising Custom errors
# In python, we can raise custom errors by using the raise keyword.
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")