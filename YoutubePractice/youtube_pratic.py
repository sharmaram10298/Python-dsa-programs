"""
# Ques 1: Write a program to print from 1 to 10.
#Solution:

i=1
while(i<=10):
    print(i)
    i=i+1
print("************")
#Ques 2:Write a program to print from 1 to n.
#Solution:
n=int(input("Enter Number: "))
i=1
while(i<=n):
    print(i)
    i=i+1
print("*****************")
#Ques 3: Write a program to print from 10 to 1.
#Solution:
i = 10
while(i>=1):
    print(i)
    i=i-1
print("*************")
#Question 4:Write a program to print from n to 1.
#Solution:

n=int(input("Enter Number: "))
while(n>=1):
    print(n)
    n=n-1
"""
"""
#Ques 5: Write a program to find sum from 10 to n.
#Solution:

n=int(input("Enter Number: "))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print("Sum = ",sum)



#Ques 6: Write a program to find sum of square from 1 to n.
#Solution:
n=int(input("Enter Number: "))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i) 
    i=i+1
print("Sum= ",sum)

#Ques 7: Write a program to find sum of cobes from 1 to n.
#Solution:
n=int(input("Enter Number: "))
i=1
sum=0
while(i<=n):
    sum=sum+i*i*i 
    i=i+1
print("Sum= ",sum)
"""

"""
#Ques 8: Write program to print only even numbers between 1 to  n.
#Solution:
#example 1:
n=int(input("Enter Number: "))
i=1
while(i<=n):
    if i%2==0:
        print(i)
    i=i+1
#example 2:
i=2
while(i<=n):
    print(i)
    i=i+2

#Ques 9: write a program to find sum of even number from 1 to n.
#Solution:
#Example 1:
n=int(input("Enter Number: "))
i=2
sum=0
while(i<=n):
    sum=sum+i
    i=i+2
print("Sum of Even numbers: ",sum)

#Example 2:
n=int(input("Enter Number: "))
i=1
sum=0
while(i<=n):
    if i%2==0:
        sum=sum+i
    i=i+1
print("Sum of Even numbers: ",sum)

"""
#Ques 10: Write a program to find sum of first n even numbers.
#Solution:
n=int(input("Enter Number: "))
i=1
sum=0
count=0
while(count<n):
    if(i%2==0):
        sum=sum+i
        count=count+1
    i=i+1
print("Sum of Even Number: ",sum)




















        
        












































