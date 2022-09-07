"""
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets,
and they have keys and values.

Syntax:
dict_name = {"key1": "value1","key2": value1}
"""

employee = {"name": "Virash","gender": "Male","age": 30}
print(employee)

# with Mixed keys 
employee = {'Name': 'Virash', 55: [1, 2, 3, 4]}
print(employee["Name"])
# print(employee[keyname][list index position])
print(employee[55])
print(employee[55][0])
print(employee[55][2])
#print(employee[2][2]) # KeyError
