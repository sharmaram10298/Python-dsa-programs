employee = {"name": "Virash","gender": "Male","age": 22}

print("\nPrint all key names in the dictionary, one by one:")
for x in employee:
  print(x)

for x in employee.keys():
  print(x)

print("\nPrint all values in the dictionary, one by one:")
for x in employee:
  print(employee[x])

print("\nYou can also use the values() function to return values of a dictionary:")
for x in employee.values():
  print(x)

print("\nLoop through both keys and values, by using the items() function:")
for x, y in employee.items():
  print(x,"=>",y)

