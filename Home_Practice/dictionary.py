"""
A dictionary is a collection which is unordered, and chaneable
and indexed. In python dictionaries are written with curly
brackets, and theys and values.

Syntax:
    dict_name = {"key1": "value1","key2": value1}
    """

"""
employee = {"name": "Virash","Gender": "Male","Age":30}
print(employee)

print("****************************************")

# with mixed keys
employee = {"Name": "Virash",55: [1,2,3,4]}
print(employee["Name"])
print(employee[55])
print(employee[55][0])
print(employee[55][2])
print(employee[55][-1:-3])# Blank dict

print("************************************")
# You can access the items of a dictionary by referring to its name, inside square brackets;

employee = {"name": " virash","Gender": "Male","Age":22}
emp_name = employee["name"]
print("Name: " , emp_name)


print("************************************")


# There is also a method called get() that will give you the same result:

employee = {"name": " virash","Gender": "Male","Age":22}
emp_gender = employee.get("Gender")
print("Gender: ",emp_gender)


print("*****************************************************")

# acess mixed keys:
employee = {"name": " virash", 1: [1,2,3,4]}
print(employee.get("name"))
print(employee[1][0])
print(employee[1][2])

print("*****************************************************")
# You access the items of a dictionary by referring  to its  key name inside  square brackets:

employee = {"name":"Virash","gender":"male","age":22}
emp_name = employee["name"]
print("Before Change Name : ",emp_name)
employee["name"]="Virash Training"
emp_name=employee.get("name")
print("After change name : ",emp_name)

print("*****************************************************")

employee = {"name":"virash","gender":"male","age":22}
print("\nPrint all key names in the dictionary, one by one")
for x in employee:
    print(x)
print("******")
for x in employee.keys():
    print(x)
print("******")
for x in employee:
    print(employee[x])
print("******")

for x in employee.values():
    print(x)
print("*******")

for x,y in employee.items():
    print(x,"=>",y)
print("***********************************************")

employee = {"name":"Virash","gender":"male","age":22}
if "name" in employee:
    print("Yes, 'name' is one of the keys in the employee dictionary")
print("**********************************")

employee = {"name":"Virash","gender":"male","age":22}
print(len(employee))

print("*******************************************")

employee = {"name":"Virash","gender":"male","age":22}
print(employee)
employee["salary"]= 50000
print(employee)
"""
"""
print("***********************************************")

employee  = {"name":"Virash","gender":"male","age":22,"salary":3000}

print(employee)
# the pop() method removes the item with the specified key name:
employee.pop("name")
print(employee)

print("*******************")

# the popitem() method removes the last inserted item:

employee.popitem()
print(employee)

print("*********************")

# The del keyword removes the item with the specified key name:
del employee["age"]
print(employee)

print("**********************")

# The clear() keyword empties the dictionary:
employee.clear()
print(employee)

print("*************************")

# The del keyword can also delete the dictionary completely.
"""
"""
del employee
print(employee) # this will cause an error because "employee" no longer exists."""
"""
# Nested Dict delete
employee = {5: 'Welcome',6: 'To',7: 'Virash',
            'A':{1:'Virash',2: 'Traning',3: 'Institute'},
            'B':{1: 'Virash',2: 'Traning',3: 'Institute'}}
print(employee)
print("****")
del employee[6]
print(employee)
print("***************")
print(employee['A'][2])
print("****")
del employee['A'][2]
print("*********************************************")

employee = {"name":"virash","gender":"male","age":22,"salary": 3000}

# Make a copy of a dictionary with the copy() method:
emp = employee.copy()
print(emp)
print("*****")
# Make a copy of a dictionary with the copy() method:
emp = dict(employee)
print(emp)

print("********************")

# Creating a Nested Dictionary
employee = {1:'Virash',2:'Traning',3:{'name':'Test','gender':'male','salary':50000}}

print(employee)
print(employee[1])
print(employee[3])
print(employee[3]["name"])

for x,y in employee.items():
    print(x,'=',y)
    if isinstance(y,dict):
        for i,j in y.items():
            print(i,'=',j)
print("*****************************************")

#Dictionary Comprehension:
#Comprehension concept application for dictionary also.
squares={x:x*x for x in range(1,6)}
print(squares)
print("***********************************")

doubles={x:2*x for x in range(1,6)}
print(doubles)
"""








def multiply(a, b):
    2*5
    print("This is sum: ")
multiply('a','b')








































































































    










































































