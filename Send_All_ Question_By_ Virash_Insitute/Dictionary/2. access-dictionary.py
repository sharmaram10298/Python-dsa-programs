# You can access the items of a dictionary by referring to its key name, inside square brackets:

employee = {"name": "Virash","gender": "Male","age": 22}
emp_name = employee["name"]
print("Name :",emp_name)

# There is also a method called get() that will give you the same result:
emp_gender = employee.get("gender")
print("Gender :",emp_gender)


# Access Mixed keys 
employee = {'Name': 'Virash', 1: [1, 2, 3, 4]} 
print(employee.get("Name"))
print(employee[1][0])
print(employee[1][2])

