#First Syntax
"""
try:
    print(1/0)
except ZeroDivisionError:
    print("You Can't divide by zero!")
"""
"""
# Second Syntax
try:
    result = 15/0
except ZeroDivisionError:
    print(" before except ")
except ZeroDivisionError:
    print("Division by Zero!")
else:
    print("result is",result)
finally:
    print("executing finally clause")
"""
#Third Syntax
"""
try:
    a = int(input("Enter a positve integer:"))
    print(a)
except ValueError:
    print("That is not a number!")
"""
#Fourth Syntax
"""
try:
    a = int(input("Enter the Positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
    print(a)
except ValueError as ve:
    print(ve)
"""
"""
#fiveth Syntax
try:
    a = int(input("Enter the firt Number"))
    b = int(input("Enter the Second Number"))
    result=a/b
except ValueError:
    print("That is not a number!")
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("result is ", result)
"""

# sixth Syntax
"""
try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter the Second Number: "))
    result = a/b
except:
    print("An unexpected error occurred")
else:
    print("result is ", result)
"""
    
