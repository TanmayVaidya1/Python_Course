def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the numbers of terms: "))

if(terms<=0):
    print("Enter any positive integers")
else:
    for i in range(terms):
        print(fibonacci(i))
  


