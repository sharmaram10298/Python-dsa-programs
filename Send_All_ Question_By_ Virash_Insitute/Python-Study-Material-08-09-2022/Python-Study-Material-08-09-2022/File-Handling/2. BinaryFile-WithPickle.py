import pickle

"""
pickle module deals with binary files. here data are not written but dumped
and similarly, data are not read but loaded. The pickle module must be imported
to load and dump data.
the pickle module provides two methods dump() and load() to work with binary
files for pickling and unpickling respectively.
"""

obj=open('student.txt','wb')
pickle.dump("Hello from Virash",obj)
obj.close()

obj=open('student.txt','rb')
data=pickle.load(obj)
print(data)
obj.close()

stud=[1,'Rakesh','Python',20000]
obj=open('student.dat','wb')
pickle.dump(stud,obj)
obj.close()

obj=open('student.dat','rb')
data=pickle.load(obj)
print(data)
obj.close()

