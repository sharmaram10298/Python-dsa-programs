"""
If we want to represent a group of unique values as a single entity then we should go
for set.
Duplicates are not allowed.
Insertion order is not preserved.But we can sort the elements.
Indexing and slicing not allowed for the set.
Heterogeneous elements are allowed.
Set objects are mutable i.e once we creates set object we can perform any changes in
that object based on our requirement.
We can represent set elements within curly braces and with comma seperation
We can apply mathematical operations like union, intersection, difference etc on set
objects.
"""

#Creation of Set Objects:
s={10,20,30,40}
print(s)
print(type(s))
      
print("************************************")
#We can create set objects by using set() Function s = set(any sequence)
#Eg 1:

l = [10,20,30,40,10,20,10]
s=set(l)
print(s) # {40, 10, 20, 30}

#Eg 2:
s=set(range(5))
print(s) #{0, 1, 2, 3, 4} 

"""
Note:
֍ While creating empty set we have to take special care.
֍ Compulsory we should use set() function.
֍ s = {} It is treated as dictionary but not empty set.
"""
s={}
print(s)
print(type(s))
print("************************************")

s=set()
print(s)
print(type(s))
print("************************************")
#Access Items
s={10,20,30}
for x in s:
    print(x)
print(len(s))
print("************************************")
"""s={10,20,30}
#Error (index and slicing not allowed in set)
for x in range(0,len(s)):
    print(s[x])"""
print("*****************add()*******************")
#Adds item x to the set.
s={10,20,30}
s.add(40);
print(s) #{40, 10, 20, 30}
print("************************************")
#To add multiple items to the set.
"""
Arguments are not individual elements and these are Iterable objects like List, Range
etc. All elements present in the given Iterable objects will be added to the set.
"""
s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)

"""
What is the difference between add() and update() Functions in Set?
We can use add() to add individual item to the Set,where as we can use update()
function to add multiple items to Set.
add() function can take only one argument where as update() function can take any
number of arguments but all arguments should be iterable objects.
"""
print("************************************")
s=set()

s.add(10)
print(s)     
print("***************add()***update()******************")
#s.add(10,20,30)#TypeError: add() takes exactly one argument (3 given)
#s.update(10)#TypeError: 'int' object is not iterable

s={10,'String',6.7}
print(s)
print("***************copy()*********************")
#copy():Returns copy of the set.It is cloned object.
s = {10,20,30}
s1 = s.copy()
print(s1)
print("*****************pop()*******************")
#pop():It removes and returns some random element from the set.
s={40,10,30,20}
print(s)
print(s.pop())
print(s.pop())
print(s)
print("******************remove()******************")
#remove(x):It removes specified element from the set.If the specified element not present in the Set then we will get KeyError.
s = {40, 10, 30, 20}
s.remove(30)
print(s)
s.remove(40)
print(s)
print("*****************discard*******************")
#discard(x):It removes the specified element from the set.
#If the specified element not present in the set then we won't get any error.
s = {10, 20, 30}
s.discard(10)
print(s)
s.discard(50)
print(s)
print("******************clear()******************")
#clear():To remove all elements from the Set.
s={10,20,30}
print(s)
s.clear()
print(s)
del s
#print(s)
print("*****************union()*******************")
#union():x.union(y) We can use this function to return all elements present in both sets.
#x.union(y) OR x|y.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.union(y))
#print (x|y)
print("**************intersection()**********************")
#intersection():x.intersection(y) OR x&y.Returns common elements present in both x and y.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.intersection(y))
print(x&y)
print("*******************difference()*****************")
#difference():x.difference(y) OR x-y. Returns the elements present in x but not in y.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.difference(y))
print (x-y)
print (y-x) 
print("******************symmetric_difference()******************")
#symmetric_difference():x.symmetric_difference(y) OR x^y.
#Returns elements present in either x OR y but not in both.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.symmetric_difference(y))
print(x^y)
print("******************Membership Operators: (in, not in)******************")
#Membership Operators: (in, not in)
s=set("virash")
print(s)

#print('v' in s)
#print('z' in s) 
#print('v' not in s)
#print('z' not in s)"""
