x=2

def test():
    global x
    y=3 #local variable
    x=x+y
    print("Inside function",x)
    print("Inside function",y)

def test1():
    print("Inside function 1",x)
    print("Inside function 1",y)
    
test()
#test1()
print("Outside function",x)
#print("Outside function",y)

