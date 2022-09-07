#First Syntax
"""
try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.

"""

#Second Syntax
"""
try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
"""

#The except Clause with No Exceptions
"""
try: 
   You do your operations here;
   ......................
except:
   If there is any exception, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
"""

#The try-finally Clause
"""
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
"""

#nested try Clause

"""
try:
   You do your operations here;
   try:
      You do your operations here;
   finally:
      This would always be executed.
except ExceptionI:
   If there is ExceptionI, then execute this block.
"""

#Example - 1

try:
    print (1/0)
except ZeroDivisionError:
    print ("You can't divide by zero")
print("****************************************")
#Example - 2

try:
    result = 5 / 1
    print("before except")
except ZeroDivisionError:
    print ("division by zero!")
else:
    print ("result is", result)
finally:
    print ("executing finally clause")
print("*****************************************")
#Example - 3

try:
    a = int(input("Enter a positive integer: "))
    print(a)
except ValueError:
    print("That is not a number!")
print("*****************************************")
#Example - 4

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
    print(a)
except ValueError as ve:
    print(ve)
print("***********************************************")
#Example - 5

try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    result=a/b
except ValueError:
    print("That is not a number!")
except ZeroDivisionError:
    print ("division by zero!")
else:
    print ("result is", result)
print("***********************************************")
#Example - 6

try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    result=a/b
except: 
    print ("An unexpected error occurred")
else:
    print ("result is", result)
