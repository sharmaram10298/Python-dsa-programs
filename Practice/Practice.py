"""1.Write a program that accepts two integers from the user and􀀁
calculate the sum of the two integers."""
"""
num1 = int(input("Enter the First Value:- "))
num2 = int(int(input("Enter the Second Value:- ")))
print(num1+num2)"""
"""
2.Write a program that accepts two integers from the user and􀀁
calculate the product of the two integers """

"""
cod1=int(input("Enter the First Product:- "))
cod2=int(input("Enter the Second Product:- "))
cal=cod1+cod2
print("Total Of product is ",cal)"""

"""
3.Write a program that accepts two integers from the user and􀀁
calculate the subtraction of the two integers."""
"""
num1=int(input("Enter the first Value: "))
num2=int(input("Enter the second value: "))
cal=num1-num2
print(cal)"""

"""
4.Write a program that accepts two integers from the user and􀀁
calculate the division of the two integers."""

"""
number1=int(input("Enter the first value: "))
number2=int(input("Enter the second value: "))
cal=number1/number2
print(cal)"""

"""
5.Write a program that accepts two integers a, b from the user and􀀁
calculate the reminder of the a/b.
"""

"""
num1=int(input("Enter the A value: "))
num2=int(input("Enter the B value: "))
cal=num1/num2
print(cal)
"""

"""
6.Write a program that accepts two floats from the user and calculate􀀁
the sum of the two floats.
"""

"""
coder1=float(input("Enter the First Value: "))
coder2=float(input("Enter the Second Value: "))
calculate=coder1+coder2
print(calculate)
"""

"""
7.Write a program that accepts two floats from the user and calculate􀀁
the product of the two floats.
"""

"""
coder1=float(input("Enter the First Value: "))
coder2=float(input("Enter the Second Value: "))
calculate=coder1+coder2
print(calculate)
"""

"""
7.Write a program that accepts two floats from the user and calculate􀀁
the product of the two floats.
"""

"""
num1=int(input("Enter the first Product: "))
num2=int(input("Enter the second Product: "))
cal=num1+num2
print("The Total of  product: ",cal)
"""

"""
8.Write a program that accepts two floats from the user and calculate􀀁
the subtraction of the two floats.
"""

"""
code1=float(input("Enter the first value: "))
code2=float(input("Enter the second value: "))
cal=code1-code2
print(cal)
print(type(cal))
"""
"""
9.Write a program that accepts two floats from the user and calculate􀀁
the division of the two floats.
"""

"""
A=float(input("Enter the first value: "))
B=float(input("Enter the second value: "))
c=A/B
print(c)
print(type(c))
"""
"""
10.Write a program that accepts two floats a, b from the user and􀀁
calculate the reminder of the a/b."""
"""
A=float(input("Enter the A value: "))
B=float(input("Enter the B value: "))
c=A/B
print(c)
print(type(c))
"""
"""
11.Write a program that calculates total, average and percentage of 5􀀁
subjects of a student. Take inputs from user."""

"""
print(" FIND AVERAGE AND PERCENTEGE ")

num1=int(input("Enter the English mark value: "))
num2=int(input("Enter the Math mark value: "))
num3=int(input("Enter the Hindi mark value: "))
num4=int(input("Enter the Science mark value: "))
num5=int(input("Enter the mrathi mark value: "))
cal=(num1+num2+num3+num4+num5)/5
print("Average:",cal)
print("")
calcu=(num1+num2+num3+num4+num5)/5*100
print("Percentage:",calcu)
"""

"""
12.Write a program to enter length and breadth of a rectangle and find􀀁
its perimeter."""

"""
l= float(input("Enter the length of the rectangle: "))
w= float(input("Enter the width of the rectangle: "))
perimeter=(l+w)*2
print("Perimeter of the rectangle is ",perimeter)
"""

"""
13.Write a program to find area of a rectangle
"""

"""
w=float(input("Enter the width of the rectangle: "))
l=float(input("Enter the length of the rectangle: "))
area=(w*l)
print("Area of the rectangle is:",area)
"""




14.Write a program to find surface area of a cuboid
A=float(input("Enter the width of the rectangle: "))
B=float(input("Enter the length of the rectangle: "))
C=float(input("Enter the heigth of the rectangle: "))
D=(A+B+C)/2
print("Area of the rectangle is:",D)

15.Write a program to find surface area of a cuboid

l=float(input("Enter the length Value: "))
w=float(input("Enter the width Value: "))
h=float(input("Enter the height Value: "))
s = (l*w*h)*2
print("Surface area is: ",s)
"""
"""
16.Write a program that accepts an employee's ID, total worked hours􀀁
of a month and the amount he received per hour. Print the employee's
ID and salary (with two decimal places) of a particular month.
"""

"""
emp=int(input("Enter the employee id: "))
w=int(input(" total work hours of a month: "))
p=int(input("Amount recevied per hour: "))
cal=w*p
print("employee ID: ",emp)
print("employee Salary: ",cal)
"""

"""
17.Write a program to calculate a bike’s average consumption from􀀁the
given total distance (integer value) travelled (in km) and spent fuel (in
litters, float number – 2 decimal point).
"""

"""
bike1=float(input("Enter the Total Distance in km: "))
bike2=float(input("Enter the total fuel spent in liters: "))
num=bike1/bike2
print("Average Consumption: ",num)
"""

"""
18.Write a C program to calculate the distance between the two points.
"""

"""
x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

# Calculating distance
d = ( (x2-x1)**2 + (y2-y1)**2 ) ** 0.5

# Displaying result
print('Distance = ' ,(d))
"""

"""
19.Write a C program to read an amount (integer value) and break the
amount into smallest possible number of bank notes.
"""

????????????????????




"""

"""
21.Write a program to convert a given integer (in days) to years,􀀁
months and days, assumes that all months have 30 days and all years
have 365 days.
"""
"""
def convert(seconds):
    seconds = seconds % (12 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# Driver program
n = 54876
print(convert(n))
"""
"""
22.Write a program to swap two numbers with using third variables.
"""
"""
num1=50
num2=60
num3=num1
num1=num2
num2=num3
print("num1 value: ",num1)
print("num2 value: ",num2)
"""
"""
23.Write a program to swap two numbers without using third variables.
"""
"""
num1=50
num2=60

num1=num1+num2
num2=num1-num2
num1=num1-num2
print("num1 value: ",num1)
print("num2 value: ",num2)
"""

"""
CONDITONAL STATEMENTS
"""
"""
1.Write a program to accept two integers and check whether they are
equal or not."""

"""
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

if num1 % num2 == 0:
    print(num1, "is Equal:", num2)
else:
    print(num1, "is not Equal: ", num2)
"""

"""
2.Write a program to check whether a given number is even or odd.
ram_sharma= int(input("Enter number: "))
"""
"""
if ram_sharma%2==0:
    print("EVEN")
else:
    print("ODD")
"""
"""
3.Write a program to check whether a given number is positive or
negative."""                                                                                                                                                        
"""
sharma= int(input("Enter a number: "))
if sharma > 0:
   print("Positive number")
else:
   if sharma < 0:
      print("Negative Number ")
   else:
print("Zero")

4.Write a program to find whether a given year is a leap year or not.
years= int(input('Enter  the year: '))

if (years%400==0) or (years%4==0 and years%100!=0):
    print('this is leap year')
else:
    print('this is not leap year')



5.Write a program to read the age of a candidate and determine
whether it is eligible for casting his/her own vote.

Age = int(input(" Enter the Age: "))


if Age>=18:
    print("Eligible")
else:
    print("Not eligible")






