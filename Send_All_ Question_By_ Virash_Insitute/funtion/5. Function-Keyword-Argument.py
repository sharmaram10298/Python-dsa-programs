def printinfo(name,age):
    print("Name : ", name)
    if(age>18):
        print("Age greater than 18")
    else:
        print("Age less than 18")
    
printinfo('virash',20)
printinfo(20,'virash')
printinfo(age=12,name='virash')
n=input("Enter Name : ")
a=int(input("Enter Age : "))
printinfo(age=a,name=n)
