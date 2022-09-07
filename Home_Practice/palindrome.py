def palind(n):
    rev=0
    z=n
    while(z>0):
        rev=rev*10+z%10
        z=z//10
    if (rev==n):
        print("Palindrome Number!")
    else:
        print("Not Palindrome Number!")
n=int(input("Enter Number: "))
palind(n)
    
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if (count==2):
        return 1
        #print("Prime Number")
    else:
        return 0
        #print("Composite Number")
n= int(input("Enter Number: "))
prime(n)
z=prime(n)
if (z==1):
    print("prime Number!")
else:
    print("Composite Number!")


x=int(input("Enter Number: "))
for i in range(1,11):
    z=x*i
    print(i,'X',x,'=',z)

x=int(input("Enter Number: "))
y=1
while(y<=10):
    z=x*y
    print(y,'X',x,'=',z)
    y=y+1















        
