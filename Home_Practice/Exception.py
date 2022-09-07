#Example - 1
try:
    print(1/0)
except ZeroDivisionError:
        print("You can't divide by zero")
#Example - 2

try:
    result = 5/1
    print("before except")
except ZeroDivisionError:
    print("Division by Zero!")
else:
    print("result is :",result)
finally:
    print("executing finally clause")

#Example - 3
try:
    a = int(input("Enter a positive integer: "))
    print(a)
except ValueError:
    print("That is not a number!")
#Exaample - 4

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
    print(a)
except ValueError as ve:
    print(ve)
#Example - 5

try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second Number: "))
    result = a/b
except ValueError:
    print("That is not a number!")
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("result is: ",result)

#Example - 6

try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter the second number: "))
    result = a/b
except:
    print("An unexpected error occured")
else:
    print("result is: ", result)
