#Loop Control Statements
# 1) break statement
#Syntax: break
#Example
"""print ("Break Statement")
x = 1                  
while x <= 10:              
    print ("Current value of x :"+ str(x))
    if x == 5:
        break
    x = x +1
print ("Good bye!")"""

# 2) continue statement
#Syntax: continue
#Example
"""
print ("Continue Statement")
x = 0                   
while x <= 10:
    x = x +1
    if x == 5:
        continue
    print ("Current variable value :", x)
print ("Good bye!")
"""

"""a=0  
while a<=5:  
    a=a+1  
    if a%2==0:  
        continue  
    print (a)  
print ("End of Loop")"""

# 3) pass statement
#Syntax: pass
#Example
"""
for x in range(1,5):
    pass

if x%2==0:
    pass

def add():
    pass

class Addition:
    pass
"""

"""
while True:
    num=int(input("enter number : "))
    
    if num==0:
        break
    elif num<0:
        continue
    else:
        print("Entered number is :",num)    
"""
