"""
#Ques 1: Write a program to find sum of digits of a given number.
i=int(input("Enter Number: "))
sum=0
while(i>0):
    sum=sum+i% 10
    i=i//10
print("Sum of digits= ",sum)

# Ques 2: Write a program  to find sum of squae of digits of a given number.

i=int(input("Enter Number: "))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("sUM OF square of each digit= ",sum)


# Ques 3: Write a program to find sum of cube of digits of a given number.
i=int(input("Enter Number: "))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print("Sum of cube of each digit= ",sum)

# Ques 4: write a program to check whether a given number is armstrong or not.
i=int(input("Enter Number to check for armstrong"))
sum=0
orig=i
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Armstrong")
else:
    print("Not armstrong")
"""
"""
# Ques 5: write a program to find product of digits of a given number.

i=int(input("Enter Number: "))
prod=1
while(i>0):
    prod=prod*(i%10)
    i=i//10
print("Product of digits= ",prod)





# Ques 6: write a program to find sum of even digits and product of add digits a given number.






# Ques 7: write a program to reverse a given number.

i=int(input("Enter Number: "))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse= ",rev)

# Ques 8: write a program to check whether a given number is palindrom number or not.

i=int(input("Enter Number: "))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print("Palindrome Number")
else:
    print("Not Palindrome")

# Ques 9: write a program to check whether a  number is prime  or not.

n=int(input("Enter Number: "))
count=0
i=1
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("Prime Number")
else:
    print("Composit Number")

# Ques 10: write a program to print factors of given number.

n=int(input("Enter Number: "))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial: ",fact)

# Ques 11: write a program to print fibonacci series upto a given number.

n=int(input("Enter Number: "))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
# Ques 10: write a program to count total number of factors of a given number.



"""
# Ques 11:

n=int(input("Enter Number: "))
i=1
while(i<=10):
    print(i,'X',n,'=',i*n)
    i=i+1












