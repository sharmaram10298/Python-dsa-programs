"""You cannot copy a list simply by typing list2 = list1,
because: list2 will only be a reference to list1, and changes made in list1 will
automatically also
be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy()."""


firstlist = ["apple", "banana", "cherry"]
print("First List =",firstlist)
secondlist = firstlist.copy()
print("Secondlist=",secondlist)

print("*********************************")
# append item in firstlist
firstlist.append(4)
print("Firstlist=",firstlist)
print("Secondlist=",secondlist)
secondlist = firstlist.copy()
print("Secondlist=",secondlist)
secondlist.append(5)
print("1st List :",firstlist)
print("2nd List :",secondlist)
print("********************built-method copy()********************")
# Another way to make a copy is to use the built-in method list()."""

firstlist = ["apple", "banana", "cherry"]
secondlist = list(firstlist)
print(secondlist)
print(firstlist)
print("*******************************************")


list1=[1,2,3]
list2=list1
print("list 1",list1)
print("list 2",list2)
list1.append(4)
print("list 1",list1)
print("list 2",list2)

print("************************************")

