employee = {"name": "Virash","gender": "Male","age": 22,"salary": 3000}

print(employee)
# The pop() method removes the item with the specified key name:
employee.pop("name")
print(employee)

# The popitem() method removes the last inserted item:
employee.popitem()
print(employee)

# The del keyword removes the item with the specified key name:
del employee["age"]
print(employee)

# The clear() keyword empties the dictionary:
employee.clear()
print(employee)

# The del keyword can also delete the dictionary completely:
"""del employee
print(employee) #this will cause an error because "employee" no longer exists."""

# Nested Dict delete
employee = { 5 : 'Welcome', 6 : 'To', 7 : 'Virash', 
        'A' : {1 : 'Virash', 2 : 'Training', 3 : 'Institute'}, 
        'B' : {1 : 'Virash', 2 : 'Training'}}
print(employee)
print("************")
del employee[6]
print(employee)
print("************")
print(employee['A'][2])
print("************")
del employee['A'][2]
print(employee)
print("************")
