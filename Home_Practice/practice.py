""" Create List"""

"""
num_list = []
print("Empty List: ",num_list)

num_list = ["mumbai","b","c"]
print("String Data Type : ",num_list)

num_list = [1,2,3]
print("integer Data Type : ", num_list)

num_list = [1, "Hello",3.4]
print("Multi-Dimensional List :",num_list)

num_list = [['a', 'b'],['c']]
print(num_list)
"""
""" Access element Fron list"""
"""
print("Posittive Indexing")
num_list = ['p','r','o','b','e']
print(num_list[0])

print(num_list[2])

print(num_list[4])

print(num_list[4.0])# Error
"""
"""
print("Negative Indexing")

num_list = ['p','r','o','b','e']

print(num_list[-1])

print(num_list[-3])

print(num_list[-5])

# Creating a Multi-Dimensinal List (By Nesting a list inside a List)

num_list = [['a','b'],['c']]

# accessing a element from the Multi-Dimensional List Using Index Number

print("Accessing a element from a Multi-Dimensional List")
print(num_list[0][1])

print(num_list[1][0])

print(num_list[1][1])#Error
"""
"""
# How to Change or add elements to a list

num_list = [2, 4, 6, 8]

print("Original List :",num_list)
# Output: [2,4,6,8]
# change the 1st item

num_list[0]=1
print("Change 0th Position :",num_list)

# Change 2nd and 4th items
# num_list[1:4] start index 1 & end index 4-1=3
num_list[1:4] = [3,5,7]
print("Change 2nd to 4th items : ",num_list)
#output: [1,3,5,7]
"""

# LOOP-THROUGH-ELEMENTS
"""
num_list = ["apple","Banana","cherry"]

for x in num_list:
    print(x)

for x in range(0,len(num_list)):
    print(num_list[x])
    print(x)
"""
"""
fact_arr=[4,5,8,6]

for num in fact_arr:
    fact = 1
    for i in range(1,num+1):
        #fact = fact*i
        print("Factorial of ",num,"is",fact)
"""

"""
rev_arr = [1221,12345,345678]

for num in rev_arr:
    rev=0
    rem=0
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print("Reverse =",rev)
"""

""" Item-exits"""
"""
num = str(input("Enter item name hear: "))
num_list = ["apple","banana","cherry"]
if num in num_list:
    print("Yes, 'apple' is in the list")
else:
    print("This item not in the list")

"""
"""
# List- lenght

num_list =["apple","banana","cherry","mango","Grapes"]
print("Lenght = ",len(num_list))
"""

# add items in the List

num_list =[1,3,5]
print("Original List : ",num_list)

# To add an item to the end of the list use the append() mehtod:
num_list.append(7)
print(num_list)

num_list.append(45)
print(num_list)

# Add item using for loop

for i in range(1,4):
    num_list.append(i)
    print("List after Addition of elements from 1-3: ",num_list)
    
# Addition of List to a List
list2 = [55,90]
num_list.append(list2)
print("List after Addition of a List :",num_list)

#  To add an item at the sepcified index, use the insert() method:
# insert(position, value)

num_list.insert(2,6)
print(num_list)

# Addition of multiple element, to the end of the current list

num_list.extend([9,11,13])
print(num_list)


num= int(input("Enter the Evn & Odd Number: "))
list1=[]
list2=list1
list2.extend(list1)
for i in range(1,num+1):
    if i%2==0:
        print("Evn Numbers")
    else:
        print("Odd numbers")































































































