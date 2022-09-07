def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    #print("Factorial of",num,"is",fact)
    return fact

x=int(input("Enter number = "))
#factorial(x)
result=factorial(x)
print("Factorial of",x,"is",result)
print("Factorial of",x,"is",factorial(x))

print("********************************************")
def voting(name,age):
    if(age>=18):
        return True
    else:
        return False
    
n=input("Enter Name : ")
a=int(input("Enter Age : "))
if(voting(n,a)):
    print("Hello",n,", you are eligible for vote")
else:
    print("Hello",n,", you are not eligible for vote")
