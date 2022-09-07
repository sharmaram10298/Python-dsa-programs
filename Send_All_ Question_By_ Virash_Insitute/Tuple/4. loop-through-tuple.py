my_tuple = ("apple", "banana", "cherry")

for x in my_tuple:
  print(x)
print("******************* ")
for i in range(0,len(my_tuple)):
  print(my_tuple[i])
print(" *********************** ")
num=(1,2,3,4,5,6)
for n in num:
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  print("factorial of",n,"is",fact)

