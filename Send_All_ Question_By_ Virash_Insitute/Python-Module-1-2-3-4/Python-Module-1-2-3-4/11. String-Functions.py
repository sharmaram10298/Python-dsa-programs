#String Functions

str1 = "virash, training, INSTITUTE virash."
str2 = "123virash"
str3 = "123456"
str4 = "virashtraining"

print(str1.capitalize()) #The capitalize() method returns a string where the first character is upper case.
print(str2.capitalize())
print(str1.count("virash")) #The count() method returns the number of times a specified value appears in the string.
print(str1.count("virash", 10, 45)) #string.count(value, start, end)
print(str1.endswith("."))#The endswith() method returns True if the string ends with the specified value, otherwise False.
print(str1.endswith("institute virash", 10, 45))#string.endswith(value, start, end)
print(str1.endswith("INSTITUTE, virash.", 10, 45))
print(str1.startswith("."))#The endswith() method returns True if the string ends with the specified value, otherwise False.
print(str1.startswith("institute virash", 10, 45))#string.endswith(value, start, end)
print(str1.startswith("virash", 0, 45))
"""
The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only difference is
that the index() method raises an exception if the value is not found.
"""
print(str1.find("virash"))
print(str1.find("INSTITUTE virash",10,45))#string.find(value, start, end)
#print(str1.index("INSTITUTE virash",10,45))#string.find(value, start, end)
#If the value is not found, the find() method returns -1, but the index() method will raise an exception:
"""
print(str1.index("virash"))
print(str1.index("Python"))
"""

print("Upper Case : ",str1.upper())
print("Lower Case : ",str1.lower())
print("Is Upper Case : ",str1.isupper())
print("Is Lower Case : ",str2.islower())

#Example of characters that are not digits: (space)!#%&? etc.
print("Is Digit : ",str2.isdigit())
print("Is Digit : ",str3.isdigit())
print("Is Numeric : ",str2.isnumeric())
print("Is Numeric : ",str3.isnumeric())
print("Is Decimal : ",str2.isdecimal())
print("Is Decimal : ",str3.isdecimal())

#Example of characters that are not alpha: (space)!#%&? etc.
print("Is Alphabates : ",str2.isalpha())
print("Is Alphabates : ",str1.isalpha())
print("Is Alphabates : ",str4.isalpha())

#Example of characters that are not alphanumeric: (space)!#%&? etc.
print("Is AlphaNumeric : ",str1.isalnum())
print("Is AlphaNumeric : ",str2.isalnum())
print("Is AlphaNumeric : ",str3.isalnum())
print("Is AlphaNumeric : ",str4.isalnum())

#The split() method splits a string into a list.
print("Split : ",str1.split())
print("Split : ",str1.split(","))
print("Split : ",str1.split(",",1))
print("Split : ",str1.split(",",2))


print("Replace : ",str1.replace("v","s"))
print("Replace : ",str1.replace("virash","vikas"))
print("Replace : ",str1.replace("VIRASH","vikas"))

print('Center :',str4.center(20,'@'))
encoding_str=str4.encode(encoding='UTF-8',errors='strict')
print('encoded :',encoding_str)
print('decoded :',encoding_str.decode(encoding='UTF-8',errors='strict'))

str5='Shalini Singh'
str6='Shalini singh'
print('Title Case :',str5.istitle())
print('Title Case :',str6.istitle())

lst=['shalini','singh']
print(lst)
print(' '.join(lst))
print(','.join(lst))

print('Length :',len(str5))

print('max :',max('a','b','c'))
print('min :',min('a','b','c','A'))
