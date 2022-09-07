"""
Type Conversion in Python

Python has two types of type conversion.
Implicit Type Conversion
Explicit Type Conversion

Implicit Type Conversion :
Python automatically converts one data type into another data type.This process doesn't need any user involvement. 
"""

"""
num_int = 123   
num_flot = 1.23  
num_new = num_int + num_flot  
print('type of num_int is : ', type(num_int))  
print('type of num_flo is : ', type(num_flot))  
print('value of num_new is : ', num_new)  
print('type of num_new is : ', type(num_new))

Output :
type of num_int is :  <class 'int'>
type of num_flo is :  <class 'float'>
value of num_new is :  124.23
type of num_new is :  <class 'float'>
"""

"""
try:  
    num_int = 123   
    num_str = '456'  
    num_new = num_int + num_str  
    print('type of num_int is : ', type(num_int))  
    print('type of num_str is : ', type(num_str))  
    print('value of num_new is : ', num_new)  
    print('type of num_new is : ', type(num_new))  
except TypeError as typeError:  
    print(typeError)  

Output :
unsupported operand type(s) for +: 'int' and 'str'
"""

"""
Explicit Type Conversion
 
Python defines type conversion functions like int(), float(), str() to directly convert one data type into another.
This type of conversion is also called typecasting because the user casts (change) the data type of the objects.

try:  
    s = "10010"      
    c = int(s)   
    print('string converted to int : ', c)  
except TypeError as typeError:  
    print(typeError)

Output :
string converted to int :  10010
"""

"""
int(s)
This function converts any data type into integer.

float(s)
This function is used to convert any data type to a floating point number.

ord(s)
This function is used to convert a character into integer (ascii value of character).

hex(s)
This function is used to convert an integer into a hexadecimal string.

oct(s)
This function converts an integer into an octal string.

tuple(s)
This function is used to convert a data type into a tuple.

try:  
    s = 'python'    
    c = tuple(s)  
    print("string converted into tuple:  ", c)  
except TypeError as typeError:  
    print(typeError)

list(s)
This function is used to convert any data type into a list type.

try:  
    s = 'python'    
    c = list(s)   
    print("string converted into list:  ", c)  
except TypeError as typeError:  
    print(typeError)

dict(tuple)
This function is used to convert a tuple of order (key, value) into a dictionary.

try:  
    tup = (('a', 1), ('f', 2), ('g', 3))  
    c = dict(tup)   
    print("tuple converted into dictionary:  ", c)  
except TypeError as typeError:  
    print(typeError)

str(s)
This function is used to convert a value (integer or float) into a string.
"""
