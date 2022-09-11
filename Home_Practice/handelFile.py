name_id=[]
name_std=[]
cls=[]
div=[]
num=0
nom=0

print("**** 1.Create Student****")
print("**** 2.Display Student****")
print("**** 3.Exit****")

virs = input("Choose a number from the above box menu 1,2,3,: ")
if virs == "1":
    while num <= nom:
        std_id=int(input("Enter Your ID:: "))
        name_id.append(std_id)
        name=input("Enter Your Name:: ")
        name_std.append(name)
        clss=int(input("Enter Your Class:: "))
        cls.append(clss)
        divs=input("Enter Your  Division::")
        div.append(divs)
        print("Enter Your ID::",end=" ")
        print(name_id[num])
        print("\nName: ",end=" ")
        print(name_std[num])
        print("Your Class::",end=" ")
        print(cls[num])
        print("Your  Division::",end=" ")
        print(div[num],end='')
        print("\n")
        mainMenu = input("Press Enter Key to go Back to MainMenu: ")
        break
elif virs == "2":
    std_id=int(input("Enter Your ID:: "))
    name_id.append(std_id)
    name=input("Enter Your Name:: ")
    name_std.append(name)
    print("Enter Your ID::",end=" ")
    print(name_id[num])
    print("\nName: ",end=" ")
    print(name_std[num])
    print("Your Class::",end=" ")
    print(cls[num])
    print("Your  Division::",end=" ")
    print(div[num],end='')

    


















    
    
