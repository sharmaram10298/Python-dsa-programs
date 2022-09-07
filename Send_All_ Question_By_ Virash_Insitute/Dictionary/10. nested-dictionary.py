 # Creating a Nested Dictionary  
employee = {1: 'Virash', 2: 'Training',3:{'name' : 'Test', 'gender' : 'Male', 'salary' : 50000}} 
print(employee) 
print(employee[1])
print(employee[3])
print(employee[3]["name"])


for x,y in employee.items():
    print(x,'=',y)
    if isinstance(y, dict):
        for i,j in y.items():
            print(i,'=',j)
