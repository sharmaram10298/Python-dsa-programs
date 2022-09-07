n = int(input("enter the number: "))
a= 0
b = 1
sum = 0
for i in range(0,n):
    print(a,end='')
    sum= sum+a
    num =a+b
    a = b
    b = num
