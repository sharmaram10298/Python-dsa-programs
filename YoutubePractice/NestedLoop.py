"""# Ques 1: Write nested loop

i=1
while i<5:
    j=1
    while j<5:
        print(j)
        j=j+1
    i=i+1
#Ques 2: peramid nestedloop
k=1
i=1
while i<=5:
    j=1
    while j<=5-i:
        print('_',end='')
        j=j+1
    b=1
    while b<=k:
        print('*',end='')
        b=b+1
    k=k+2
    print()
    i=i+1
       i=i+1
   
#Ques 2: peramid nestedloop
i=1
while i<20:
    j=1
    while j<=i:
        print('*',end='')
        j=j+1
    print()
    i=i+1

       """
#Ques 2: peramid nestedloop
k=int(input("Enter Number: "))
i=1
while(k>0):
    j=1
    while (j<i):
        print('',end='')
        j=j+1
    b=1
    while (b<=(k*2)-i):
        print('*',end='')
        b=b+1
    
    print()
    k=k-15
    i=i+1














    
