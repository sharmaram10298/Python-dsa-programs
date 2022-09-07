#Class

class Add:
    a=10
    b=20
ob=Add()
c=ob.a+ob.b
print(c)

print("*****************")

class show:
    a=10
    b=20
    def test(self):
        print("variable a= ",self.a)
        print("variable b= ",self.b)
    def show(self):
        self.test()

obj = show()
print("A= "+str(obj.a))
obj.show()

print("***********CLASS***************")

class Addition:
    def add(self,a,b):
        print('addition = '+str(a+b))
ob = Addition()
ob.add(int(input("Enter First Number: ")),int(input("Enter second Number: ")))

print("************CLSSSS******************")     

class Student:
    name=""
    div=""
    marks=0
    def setData(self,name,div,marks):
        self.name=name
        self.div=div
        self.marks=marks
    def getData(self):
        print('Name = ',self.name)
        print('Div = ',self.div)
        print('Marks = ',self.marks)
ob = Student()
ob.setData('Hello world','A',329)
ob.getData()

print("*******************Constructor*******************")

#### Constructor

# no-parameterized Constructor

class Student:
    name=""
    div=""
    marks=0
    def __init__(self):
        self.name='hello World'
        self.div='A'
        self.marks=78
    def getData(self):
        print('Nmae = ',self.name)
        print('Div = ',self.div)
        print('Marks  = ',self.marks)
ob = Student()
ob.getData()

# Paramaterized Constructor
class Student:
    name=""
    div=""
    marks=0
    def __init__(self,name,div,marks):
        self.name=name
        self.div=div
        self.marks=marks
    def getData(self):
        print("Name = ",self.name)
        print("Div = ",self.div)
        print("Marks = ",self.marks)
ob = Student(input("Enter Name: "),input("Enter Division: "),int(input("Enter Marks: ")))
ob.getData()
                 





















        















    







    















