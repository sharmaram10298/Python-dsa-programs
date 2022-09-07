"""What is tuple?
In Python programming, a tuple is similar to a list.
The main difference between lists and a tuples
is the fact that lists are mutable whereas tuples are immutable.
A mutable data type means that a python object of this type can be modified.
The difference between the two is that we cannot change the elements of a tuple once
it is assigned
whereas in a list, elements can be changed.
A Tuple is a collection of Python objects separated by commas.
In someways a tuple is similar to a list in terms of indexing,
nested objects and repetition but a tuple is immutable unlike lists which are mutable.
Note: In case your generating a tuple with a single element,
make sure to add a comma after the element.
"""

#Creating a Tuple
# empty tuple
my_tuple = ()
print(my_tuple)
# Output: ()

# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)
# Output: (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
# Output: (1, "Hello", 3.4)

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple
print("a= ",a)
print("b= ",b)
print("c= ",c)
# Output:
# 3
# 4.6
# dog
my_new_tuple = 3, 4.6, "dog","kittu",5,3,"lalli"

(p,q,*r) = my_new_tuple
print("P= ",p)
print("Q= ",q)
print("R= ",r)



print("\U0001F600")
print("\U0001F601")
print("\U0001F605")
print("\U0001F923")
print("\U0001F602")
print("\U0001F642")
print("\U0001F607")
print("\U0001F60D")
print("\U0001F612")
