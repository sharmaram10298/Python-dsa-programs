
my_list = ['p','r','o','b','l','e','m']
print("as is it:",my_list)
print("*********************************")
# The remove() method removes the specified item:
my_list.remove("r")
print("Changes remove 'r' : ",my_list)
print("*******************************")
# The pop() method removes the specified index, (or the last item if index is not specified):
my_list.pop()
print(my_list)
my_list.pop(3)
print(my_list)

print("**************************************")
# The del keyword removes the specified index:
del my_list[2]    
print(my_list)
print("**********************************")
# delete multiple items
del my_list[1:5]  
print(my_list)
print("**********************************")
# We can also use the clear() method to empty a list.
my_list.clear()
print(my_list)
print("***************************************")
# The del keyword can also delete the list completely:
del my_list       
print(my_list)
print('******************************************')
