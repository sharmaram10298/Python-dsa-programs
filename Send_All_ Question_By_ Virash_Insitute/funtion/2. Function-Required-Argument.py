def voting(name,age):
    if(age>=18):
        print("Hello",name,", you are eligible for vote")
    else:
        print("Hello",name,", you are not eligible for vote")        

n=input("Enter Name : ")
a=int(input("Enter Age : "))
voting(n,a)

#voting(n) #Error
