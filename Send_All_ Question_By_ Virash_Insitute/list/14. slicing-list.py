# Creating a List 
List = ['V','I','R','A','S','H','T','R'\
        ,'A','I','N','I','N','G','I','N'\
        ,'S','T','I','T','U','T','E'] 
print("Intial List: ")
print(List)

# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-7: ") 
print(Sliced_List) 
  
# Print elements from beginning 
# to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 
  
# Print elements from a  
# pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(Sliced_List) 
  
# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 
  
# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[5:13:2] 
print("\nPrinting List: ") 
print(Sliced_List)

Sliced_List = List[-5:-13:-2] 
print("\nPrinting List: ") 
print(Sliced_List) 

Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List)

Sliced_List = List[-5:10:-2] 
print("\nPrinting List: ") 
print(Sliced_List) 


Sliced_List = List[5:-10:2] 
print("\nPrinting List: ") 
print(Sliced_List) 
