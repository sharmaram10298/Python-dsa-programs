class Add:
    a=10
    b=20

ob=Add()
c=ob.a+ob.b
print(c)
print("*******************")

class Show:
    a=10
    b=20
    def test(self):
        print("variable a =",self.a)
        print("variable b =",self.b)
    def show(self):
        self.test()
       
obj = Show()
print("A = "+str(obj.a))
obj.show()

print("***************************")

class Addition:
    def add(self,a,b):
            print('addition = '+str(a+b))
    
ob = Addition()
ob.add(int(input("Enter 1st No. : ")),int(input("Enter 2nd No. : ")))
print("******************************")

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
ob.setData('Minu','A',78)
ob.getData()
