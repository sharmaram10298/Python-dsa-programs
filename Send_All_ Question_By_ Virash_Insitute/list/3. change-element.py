"""How to change or add elements to a list?
List are mutable, meaning, their elements can be changed unlike string or tuple.
We can use assignment operator (=) to change an item or a range of items."""

my_list = [2, 4, 6, 8]
print("Original List :",my_list)
# Output: [2, 4, 6, 8]
# change the 1st item    
my_list[0] = 1            
print("Change 0th Position :",my_list)
# Output: [1, 4, 6, 8]

# change 2nd to 4th items
#my_list[1:4] = start index 1 & end index 4-1=3
my_list[1:4] = [3, 5, 7]  
print("change 2nd to 4th items :",my_list)
# Output: [1, 3, 5, 7]
