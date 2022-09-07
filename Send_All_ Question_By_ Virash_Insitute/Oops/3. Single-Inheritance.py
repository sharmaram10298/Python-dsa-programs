"""
Inheritance allows us to define a class that inherits all the methods and properties
from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""
#inheritance
class Department:
  def __init__(self, dname, loc):
    self.deptname = dname
    self.location = loc
  def printdetails(self):
    print(self.deptname, self.location)

#Use the Department class to create an object, and then execute the printname method:

#obj = Department("IT", "Mumbai")
#obj.printdetails()



class Employee(Department):
  pass

#Use the pass keyword when you do not want to add any other properties
#or methods to the class.
obj = Employee("CS", "Pune")
obj.printdetails()

"""

class Employee(Department):
  def __init__(self, age, salary):
    self.eage = age
    self.esalary = salary
  def printempdetails(self):
    print(self.eage, self.esalary)

obj = Employee(25,15000)
obj.printempdetails()
obj.printdetails()


"""
"""
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
"""

"""
class Employee(Department):
  def __init__(self, dname, loc, age, salary):
    self.eage = age
    self.esalary = salary
    Department.__init__(self, dname, loc)
  def printempdetails(self):
    print(self.deptname, self.location, self.eage, self.esalary)

obj = Employee("IT","Goa",25,15000)
obj.printdetails()
obj.printempdetails()


Python also has a super() function that will
make the child class inherit all the methods and properties from its parent:
By using the super() function, you do not have to use the name of the parent element,
it will automatically inherit the methods and properties from its parent.



class Employee(Department):
  def __init__(self, dname, loc, age, salary):
    self.eage = age
    self.esalary = salary
    super().__init__(dname, loc)
  def printempdetails(self):
    print(self.deptname, self.location, self.eage, self.esalary)

obj = Employee("IT","Goa",25,15000)
obj.printdetails()
obj.printempdetails()
print(obj.deptname)
print(obj.location)
print(obj.eage)
print(obj.esalary)
"""
