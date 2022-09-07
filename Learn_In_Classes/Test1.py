num1=int(input("Enter the math number:- "))
num2=int(input("Enter the English number:- "))
num3=int(input("Enter the Hindi number:- "))
num4=int(input("Enter the Scince Number:- "))
num5=int(input("Enter the S. Scince number:- "))
num=(num1+num2+num3+num4+num5)/500
calcu=(num)*100
print("Percentage:",calcu,"%")

if (num1 >=90):
    print("First Division")
elif (num2>=80):
    print("Second Division")
elif (num3>=70):
    print("Third Division")
else:
    print("Fail")
