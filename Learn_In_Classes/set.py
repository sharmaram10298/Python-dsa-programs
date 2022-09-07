
s = {10,20,30,40}
print(s)
print(type(s))

# We can create set objects by using set() funtion s= set(any sequence)
# Eg1
print('********************************')
l = [10,20,30,40,10,20,10]
s = set(l)
print(s)
print('********************************')
#eg2

s = set(range(5))
print(s)
print('********************************')
# dict

s={}
print(s)
print(type(s))
print('********************************')
#set

s = set()
print(s)
print(type(s))
print('********************************')
# Access Items

s = {10,20,30}
for x in s:
    print(x)
print(len(s))
print('********************************')
"""
#Error

s = {10,20,30}
print(s[x])
"""
print('********************************')

#Adds items

s = {10,20,30}
s.add(40);
print(s)
print('********************************')
# To add multiple items to the set
s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)
print('********************************')
#add() funtion

s=set()
print(s)
s.add(10)
print(s)
print('********************************')
#s.add(10,20,30)#TypeError: add() takes exactly one argument (3 given)
# s.update(10)#TypeError: 'int'object is not iterable
s={10,'String',6.7}
print(s)

#copy():Returns copy of the set.it is cloned object.
s= {10,20,30}
s1=s.copy()
print(s1)
print('********************************')
#pop():It removes and returns some random element from the set.

s={40,10,30,20}
print(s)
print(s.pop())
print(s.pop())
print(s)

print('********************************')
"""
#remove(x):It remove the specified element from the set.if the specified element not present in the
s= {40,10,30,20}
s.remove(50)
"""
print('********************************')
#discard(x):It removes the specified element from the set.
#If the specified element not present in the set then we won't get any error
s= {10,20,30}
s.discard(10)
print(s)
s.discard(50)

print('********************************')
#union():x.union(y)
#x.union(y)OR x|y.
x = {10,20,30,40}
y = {30,40,50,60}
print(x.union(y))
print(x|y)
print('********************************')
# difference():x.difference(y)ORx-y.

x= {10,20,30,40}
y = {30,40,50,60}
print(x.difference(y))
print(x-y)
print(y-x)

print('********************************')
"""
#symmetric_difference():x.symmetric_difference(y)OR x^y.

x ={10,20,30,40}
y= {30,40,50,60}
print(x.symmetric_diffrence(y))
print(x^y)
"""
print('********************************')
#Membership Operators:(in, not in)

s= set("virash")
print(s)
print('v' in s)
print('i' in s)
print('r' in s)
print('a' in s)
print('s' not in s)
print('h' not in s)

print('********************************')
# PRACTICE



l = [10,20,30,40,50,60]

s=set(l)

print(type(s))
s=set(range(10))
print(type(s))




































































