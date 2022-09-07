
print("*********************using nine number in param funtion  **********************")

def Traning(*args):
	
	# using len() method in args to count
	return(len(args))


a = 1
b = 3

# arguments passed
n = Traning(1, 2, 4, a)

print(" The number of arguments are: ", n)
