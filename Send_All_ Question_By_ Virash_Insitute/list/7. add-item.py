my_list = [1, 3, 5]
print("Original List :",my_list)
print("***************************")
# To add an item to the end of the list, use the append() method:
my_list.append(7)
print("Add element: ",my_list)

my_list.append(45)
print("Add element: ",my_list)
print("******************************************")
# Add item using for loop
for i in range(1,4): 
    my_list.append(i) 
print("List after Addition of elements from 1-3 :",my_list)
print("***************************************")
# Addition of List to a List 
List2 = [55, 90] 
my_list.append(List2) 
print("List after Addition of a List :",my_list)  
print("*****************************************")
# To add an item at the specified index, use the insert() method:
# insert(position,value)
my_list.insert(2,6)
print(my_list)
print("***********************************")
# Addition of multiple elements, to the end of the current list
my_list.extend([9, 11, 13])
print(my_list)
