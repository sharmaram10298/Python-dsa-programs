my_list = ["apple", "banana", "cherry"]

for x in my_list:
  print(x)
print("******************************************")
for x in range(0,len(my_list)):
  print(my_list[x])
  print(x)

print("***************************************")

fact_arr=[4,5,8,6]

for num in fact_arr:
  fact=1
  for i in range(1,num+1):
    fact=fact*i
  print("Factorial of",num,"is",fact)

print("*************************************")


rev_arr=[1221,12345,345678]

for num in rev_arr:
  rev=0
  rem=0
  while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
  print("Reverse =",rev)

