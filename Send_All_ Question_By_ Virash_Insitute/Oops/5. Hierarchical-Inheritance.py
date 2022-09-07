#Hierarchical inheritance More than one derived classes are created from a single base.
class Department:
  def __init__(self, dname, loc):
    self.deptname = dname
    self.location = loc
  def printdetails(self):
    print(self.deptname, self.location)

class Employee(Department):
  def __init__(self, dname, loc, age, salary):
    self.eage = age
    self.esalary = salary
    super().__init__(dname, loc)
  def printempdetails(self):
    print(self.deptname, self.location, self.eage, self.esalary)

class Student(Department):
  def __init__(self, dname, loc, std, div):
    self.stud_std = std
    self.stud_div = div
    super().__init__(dname, loc)
  def printstuddetails(self):
    print(self.deptname, self.location, self.stud_std, self.stud_div)

obj = Employee("IT","Goa",25,15000)
obj.printdetails()
obj.printempdetails()
obj1 = Student("IT","Goa","12th","A")
obj1.printdetails()
obj1.printstuddetails()

