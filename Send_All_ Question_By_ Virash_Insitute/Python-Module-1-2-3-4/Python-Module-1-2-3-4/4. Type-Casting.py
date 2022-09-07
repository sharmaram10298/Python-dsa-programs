# Type Casting Program
"""id=int(input("Enter your id : "))
name=input("Enter your name : ")
age=int(input("Enter your age : "))
salary=float(input("Enter your salary : "))
address=input("Enter your address : ")
is_married=bool(input("Married ? : "))"""

id=eval(input("Enter your id : "))
name=input("Enter your name : ")
age=eval(input("Enter your age : "))
salary=eval(input("Enter your salary : "))
address=input("Enter your address : ")
is_married=eval(input("Married ? : "))

print("id = ",id," || Type = ",type(id))
print("name = ",name," || Type = ",type(name))
print("age = ",age," || Type = ",type(age))
print("salary = ",salary," || Type = ",type(salary))
print("address = ",address," || Type = ",type(address))
print("is_married = ",is_married," || Type = ",type(is_married))

"""a=10
b=20
c=45
print(eval("((a+b+c)-b)*a"))"""
