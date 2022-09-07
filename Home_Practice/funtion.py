"""
def virash(a,b,c,d,e,):
    vir=a+s+d+f+g
    bug=vir/500*100
    print("Total marks: ",vir)
    print("Total Percentage: ",bug)
a = int(input("maths marks: "))
s = int(input("maths marks: "))
d = int(input("maths marks: "))
f = int(input("maths marks: "))
g = int(input("maths marks: ")) 
virash(a,s,d,f,g)
"""
"""
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
x=int(input("Enter Number: "))
factorial(x)
result=factorial(x)
print("Factorial of",x,"is",result)
print("Factorial of ",x,"is",factorial(x))
print("************************************")

def voting(name,age):
    if(age>=18):
        return True
    else:
        return False
n=input("Enter Name: ")
a=int(input("Enter Age: "))
if(voting(n,a)):
    print("Hello",n,",you are eligible for vote")
else:
    print("Hello",n,",you are not eligible for vote")

print("******************************************")
"""
def printinfo(name='xyz',age=35):
    print("Name : ",name)
    print("Age : ",age)

#Now you call printinfo funtion
printinfo(age=20,name="virash")
printinfo(name="virash")
printinfo()
printinfo('shalini')
printinfo('doller',23)
printinfo(age=20)

print("****************************************")

def printinfo(name,age):
    print("Name : ",name)
    if(age>=18):
        print("Age grater than 18")
    else:
        print("Age less than 18")
printinfo('virash',20)
#printinfo(20','virash')
printinfo(age=12,name='virash')
n=input("Enter Name : ")
a=int(input("Enter Age : "))
printinfo(age= a,name=n)

























    
