#How to access elements from a list?
"""We can use the index operator [] to access an item in a list.
Index starts from 0. So, a list having 5 elements will have index from 0 to 4.
Trying to access an element other that this will raise an IndexError.
The index must be an integer. We can't use float or other types,
this will result into TypeError."""

print("Positive Indexing") 
my_list = ['p','r','o','b','e']
print(my_list[0])

print(my_list[2])

print(my_list[4])

# Error! Only integer can be used for indexing
#my_list[4.0]

"""Negative indexing
Python allows negative indexing for its sequences.
The index of -1 refers to the last item, -2 to the second last item and so on."""

print("Negative Indexing") 
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-3])

print(my_list[-5])

# Creating a Multi-Dimensional List (By Nesting a list inside a List) 
my_list = [['a', 'b'] , ['c']] 
  
# accessing a element from the Multi-Dimensional List using index number 
print("Acessing a element from a Multi-Dimensional list") 
print(my_list[0][1]) 
print(my_list[1][0])
print(my_list[1][1]) # Error
