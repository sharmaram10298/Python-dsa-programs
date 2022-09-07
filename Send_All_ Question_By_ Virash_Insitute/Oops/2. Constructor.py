#non-parameterized constructor
class Student:
    name=""
    div=""
    marks=0
    def __init__(self):
            self.name='Minu'
            self.div='A'
            self.marks=78
    def getData(self):
            print('Name = ',self.name)
            print('Div = ',self.div)
            print('Marks = ',self.marks)
    
ob = Student()
ob.getData()
print("***********************************************")
#Paramaterized Constructor
class Student:
    name=""
    div=""
    marks=0
    def __init__(self,name,div,marks):
            self.name=name
            self.div=div
            self.marks=marks
    def getData(self):
            print('Name = ',self.name)
            print('Div = ',self.div)
            print('Marks = ',self.marks)
    
ob = Student(input("Enter Name : "),input("Enter Division : "),int(input("Enter Marks : ")))
ob.getData()

print("**********************************************************************")
print('Param Constructor')
class Calculator:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def add(self):
        res=self.num1+self.num2
        return res
    
x=int(input('1st : '))
y=int(input('2nd : '))
calc=Calculator(x,y)
A=calc.add()
print(A)
print(calc.add())

print("*********************************************************")
class Calculator1:
    def __init__(self):
        self.num1=int(input('1st : '))
        self.num2=int(input('2nd : '))
    def add(self):
        res=self.num1+self.num2
        return res

print('Non Param Constructor')
calc=Calculator1()
print(calc.add())

