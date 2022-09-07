# You can access the items of a dictionary by referring to its key name, inside square brackets:

employee = {"name": "Virash","gender": "Male","age": 22}
emp_name=employee["name"]
print("Before Change Name :",emp_name)
employee["name"]="Virash Training"
emp_name=employee.get("name")
print("After Change Name :",emp_name)

