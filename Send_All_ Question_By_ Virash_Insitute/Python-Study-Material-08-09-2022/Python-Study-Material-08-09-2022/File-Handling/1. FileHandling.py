#File Handling

#Write in a file - for writing single string
"""obj=open("vti.txt","w")  
obj.write("Hello From VTI. \nVirash training Institute. \nVirash Technologies")  
obj.close()"""

#Writelines in a file - for writing sequence of strings
#(we need to pass an iterable objects like lists,tuple etc)
"""lines=["Hello From VTI\n","Welcome To Virash\n"]
obj=open("vti.txt","w")  
obj.writelines(lines)  
obj.close()"""

#Append in a file
"""obj=open("vti.txt","a")  
obj.write("\nHello Virash")  
obj.close()"""

#Read from file
# readline([n])
"""this method reads one complete line from a file where each line terminates with a
newline(\n) character. It can also be used to read a specified number(n) of bytes of
data from a file but maximum up to the newline character(\n)."""

"""
obj1=open("vti.txt","r")  
#s=obj1.readline()
#s=obj1.readline(10)
#s=obj1.readline(100)
print(s)  
obj1.close()"""

# read(n)
"""this method is used to read a specified number of bytes of data from a file.
if no argument or a negative number is specified in read(), the entire file
content is read"""

"""
obj1=open("vti.txt","r")  
##s=obj1.read(10)
##s=obj1.read(-10)
##s=obj1.read()
print(s)  
obj1.close()
"""

"""obj2=open("vti.txt","r")  
s1=obj2.read(10)  
print(s1)
s1=obj2.read(10)  
print(s1)
#check current position
position=obj2.tell()
print("Current File Position :",position)
#reposition pointer at the beginning once again
position=obj2.seek(0)
s1=obj2.read(10)  
print(s1)
obj2.close()
"""

"""
obj3=open("vti.txt","r")  
s=obj3.readlines()  
##print(s)  
obj3.close()

for data in s:
##    First Method
##    print(data,end='')
    
##    Second Method - split() - display each word of a line separately as an element of list
##    words=data.split()
##    print(words)

##    Third Method - splitlines() - line is returned as element of list
##    words=data.splitlines()
##    print(words)
"""

#Attributes of File

"""obj = open("vti.txt", "w")  
print  ("File Name : "+ str(obj.name))  
print  ("File Mode : "+ str(obj.mode))  
print  ("Before Closing File : "+ str(obj.closed))  
obj.close()
print  ("After Closing File : "+ str(obj.closed))"""

#Methods of File

#Rename file
"""import os  
os.rename('vti.txt','virash.txt')"""

#Remove file
"""import os  
os.remove('virash.txt')"""

# Get current working directory
"""import os
print('Current Directory :',os.getcwd())"""

#Make Directory & Change Directory 
"""import os  
os.mkdir("virash_new")
##if not os.path.exists("virash_new"):
##    os.mkdir("virash_new")
os.chdir("virash_new")  
obj=open("vti.txt","w")  
obj.write("Hello From VTI. Virash training Institute. Virash Technologies")  
obj.close()"""

# Remove Directory
"""import os  
#os.mkdir("virash_new1")
os.chdir("virash_new")
os.remove('vti.txt')
os.chdir("../")
os.rmdir("virash_new")"""

# Open file using with clause
"""
The advantage of using with clause is that any file that is opened using this
clause is closed automatically, once the control comes outside the with clause.
Here we don't have to close the file explicitly using close() statement.
Python will automatically close the file.
"""

with open("vti.txt", 'w') as file:
    file.write("Hello from Virash")
