num = int(input("Enter any number : "))
print("your number is ",num)
if(num<0):
    print("the number is negative")
elif(num>0):
    if(num<=10):
        print("the number is between 1-10")
    elif(num>10 and num<=20):
       print("the number is between 11-20") 
    else:
        print("the number is greater than 20")       
else:
    print("the number is zero")
    