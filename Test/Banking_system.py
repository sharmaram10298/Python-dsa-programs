num1 = [] # Name account holder
num2A = []# Account Number
num4B = []# Balance 
num5D = 0 # Deposit Amount
num6W = 0 # Withdraw amount
num7 = 0
num8 = 0
num9 = 0
num = 0

while True:
    print("(*******************************************************************)")
    print("(******************** VIRASH TRAINING INSTITUTE **********************)")
    print("(*******************************************************************)")
    print("")
    print("(---------------------  BANKING  SYSTEM HEAR  -------------------)")
    print("(---------------------  (a). Create New Account.  ------------)")
    print("(-----------------------  (b). Withdraw a Amount.   ------------)")
    print("(------------------------  (c). Deeposit Amount.     ------------)")
    print("(-------------------------  (d). Check Balance.       -----------)")
    print("(--------------------------- (e). Quit.                 ---------)")
    print("")
    print("(********************************************************************)")
    print("(******************** VIRASH TRAINING INSTITUE **********************)")
    print("(*******************************************************************)")
    print("")

    Virash = input("Choose a Letter from the Above Box menu a, b, c, d, e, : ")
    if Virash == "a":
        print("Thank For Choosing 'a'! ")
        print("Please Fill the All Details and Open Your Account!")

        while num8 <= num:
            name = input("Enter Your Fullname: ")
            num1.append(name)
            Account_number = int(input("Please Create Your Account Number: "))
            num2A.append(Account_number)
            num4c = 0
            num5D = int(input("Please Deposit Amount to start Your Account: "))
            num4c = num4c + num5D
            num4B.append(num4c)
            print("\nName: ",end=" ")
            print(num1[num9])
            print("Your Account Number: ",end=" ")
            print(num2A[num9])
            print("Blance Amount: ",end=" ")
            print(num4B[num9],end='')
            print("\n-----  Your Account created successfully! --------")
            print("\n")
            print("Note! Please remember The Name and  Your Account Number")
            mainMenu = input("Press Enter Key to go Back to MainMenu: ")
            break
    elif Virash == "b":
        com = 0
        print("Thanks For Choosing 'b'! ")
        print("Please Fill the required Details and Withdraw Your Amount!")
        while com < 1:
            vir = -1
            name = input("Enter Accountholder FullName: ")
            Ac_number = int(input("Enter Your Account Number: "))
            while vir < len(num1)- 1:
                vir = vir + 1
                if name == num1[vir]:
                    if Ac_number == num2A[vir]:
                        com = com + 1
                        print("Your Current Balance this: ", end=' ')
                        print(num4B[vir],end=" ")
                        print("\n")
                        num4c = (num4B[vir])
                        num6W = int(input("Enter Amount to Withdraw : "))
                        if num6W > num4c:
                            deposit = input("Please Deposit Your Amount: ")
                            num4c = num4c + deposit
                            print("Your Current Balance: ",end+" ")
                            print(num4c,end=" ")
                            num4c = num4c - num6W
                            print("\n")
                            print("---- Withdraw Successfully!------")
                            num4B[w] = num4c
                            print("Your Current Balance: ", num4c,end=" ")
                            print("\n")
                        else:
                            num4c = num4c - num6W
                            print("\n")
                            print("----- Withdraw Successfully -----")
                            num4B[vir] = num4c
                            print("Your Current Balance: ", num4c,end=" ")
                            print("\n")
                if com < 1:
                        print("Your nmae and Account does not match!\n")
                        mainMenu = input("Press Enter Key to go Back to MainMenu: ")
                        break
    elif Virash == "c":
        print("Thank you For Choosing 'c'!")
        a = 0
        while a < 1:
            vir = -1
            name = input("Enter Your Fullname: ")
            Ac_number = int(input("Enter Your Account number : "))
            while vir < len(num1) - 1:
                vir = vir + 1
                if name == num1[vir]:
                    if Ac_number == num2A[vir]:
                        a = a + 1
                        print("Your Current Balance: ",end=" ")
                        print(num4B[vir],end=" ")
                        num4c = (num4B[vir])
                        print("\n")
                        num5D = int(input("Enter the Deposit Amount: "))
                        num4c = num4c + num5D
                        num4B[vir] = num4c
                        print("\n")
                        print("----- Deposit Amount Successfully! -------")
                        print(" Your Current Balance : ", num4c,end=" ")
                        print("\n")
            if a < 1:
                print("Your nmae and Account does not match!\n")
                break
        mainMenu = input("Press Enter Key to go Back to MainMenu: ")
    elif Virash ==  "d":
            print("thank you for selected 'd'!")
            vir = 0
            print("Client name list and balances mentioned below : ")
            print("\n")
            while vir <= len(num1)-1:
                print("->.Customer =",num1[vir])
                print("->. Balance =", num4B[vir],end='')
                print("\n")
                vir = vir + 1
            mainMenu = input("Press Enter Key to go Back to MainMenu: ")
    elif Virash == "e":
         print("Than you for using banking system!!")
         print("have a Good day!")
         break
    else:
        print("Invalid option selected please try again!")
        mainMenu = input("Press Enter Key to go Back to MainMenu: ")
            
     
            
                            
             
                    
                
                
        
            















            
            
            
