num1=int(input(" Enter the first number:- "))
num2=int(input("Enter the second number:- "))
num3=int(input("Enter the third number:- "))
num4=int(input("Enter the four Number:- "))
num5=int(input("Enter the five number:- "))
cal=float(num1+num2+num3+num4+num5)/5
print("Average:",cal)
calcu=(num1+num2+num3+num4+num5)/500*100
print("Percentage:",calcu,"%")

if (num1 >=85):
    print(" First Division")
elif (num2>=75):
    print("Second Division")
elif (num3>=60):
    print("Third Division")
else:
    print("Fail")
    

