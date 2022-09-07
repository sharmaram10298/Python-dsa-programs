# i) string concatention

print('hello'+'world')
a='virash'
b='training'
print(a+b)

# ii) string with number

name='virash'
age=5
salary=15000
print(name+str(age))

# iii) String Formatting with the { } Operators

"""
When you use the curly braces or {} operators, they serve as place-holders for the
variables
you would like to store inside a string. In order to pass variables to a string you must call
upon the format() method.One benefit of using the format() method is that you do not have to
convert integers into a string before concatenating the data. It will do that automatically for you.
This is one reason why it is the preferred operator method.
"""

print ("Name = {} Age = {} Salary = {}".format(name,age,salary))
#print ("Age = {1} Name = {0} Salary = {}".format(name,age,salary)) # Error
print ("Name = {0} Age = {1} Salary = {2}".format(name,age,salary))
print ("{2} {0} {1}".format(name,age,salary))
name = "Virash {} {}."
print(name.format("Training","Institute"))
name = "Virash {1} {0}."
print(name.format("Training Institute",25))
print("Virash {0} {1} {course}.".format("Training", "Institute", course = "provides python course"))

# iv) new line

x=10
y=20
z=30
print("x = "+str(x)+"\ny = "+str(y)+"\nz = "+str(z))
