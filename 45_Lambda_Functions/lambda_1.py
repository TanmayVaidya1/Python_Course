# Lambda Functions in Python
# In Python, a lambda function is a small anonymous function without a name. 
# It is defined using the lambda keyword and has the following 

# syntax:
# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for
# a short period of time. They are commonly used as arguments to higher-order functions, 
# such as map, filter, and reduce.

# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
double = lambda x: x * 2
print(double(5))