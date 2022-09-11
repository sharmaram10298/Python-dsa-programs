"""
What are lambda functions in Python?
In Python, an anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, anonymous
functions are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.

Syntax
lambda arguments : expression

Lambda functions can have any number of arguments but only one expression.
The expression is evaluated and returned.
"""

# Program to show the use of lambda functions
"""double = lambda x: x * 2
print(double(5))"""

"""
In the above program, lambda x: x * 2 is the lambda function.
Here x is the argument and x * 2 is the expression that gets evaluated and returned.
This function has no name. It returns a function object which is assigned to the identifier double.
We can now call it as a normal function. The statement

double = lambda x: x * 2

is nearly the same as:

def double(x):
   return x * 2

   double(6)
"""

#print((lambda x: x + 1)(2))

#Lambda functions can take any number of arguments:
#Multiply argument a with argument b and return the result:
"""x = lambda a, b : a * b
print(x(5, 2))"""

"""full_name = lambda first, last:'Full name: '+str(first)+' '+str(last)
print(full_name('Virash','Training'))"""

#Summarize argument a, b, and c and return the result:
"""x = lambda a, b, c : a + b + c
print(x(1, 2, 3))"""

#The power of lambda is better shown when you use them as an anonymous function inside another function.
"""def myfunc(n):
  return lambda a : a * n

x = myfunc(2)
print(x(5))
x = myfunc(3)
print(x(5))"""

"""
#Required Argument
print((lambda x, y, z: x + y + z)(1, 2, 3))
#Default Argument
print((lambda x, y, z=3: x + y + z)(10, 20))
#Keyword Argument
print((lambda x, y, z: x + y + z)(x=1, y=2,z=3))
"""

#map : map(function, iterable)
"""print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)"""

#filter : filter(function, iterable)
"""print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow'])))
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)"""

#reduce : functools.reduce(function, iterable[, initializer])
"""from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))"""
"""
Apply function of two arguments cumulatively to the items of iterable, from left to right,
so as to reduce the iterable to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
The left argument, x, is the accumulated value and the right argument, y, is the update value
from the iterable.
"""
#print(reduce(lambda acc, x:acc+' | '+x, ['cat', 'dog', 'cow']))
