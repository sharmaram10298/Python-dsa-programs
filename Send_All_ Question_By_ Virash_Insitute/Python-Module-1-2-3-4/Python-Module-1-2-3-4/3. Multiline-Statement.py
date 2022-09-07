# 1. Python Single-line Statements

num=10  # statement 1
sum=num+10  # statement 2
print(sum)  # statement 3

# 2. Python Multi-line Statements

"""
Python statements are usually written in a single line. The newline character marks the end of the
statement. If the statement is very long, we can explicitly divide into multiple lines with the line
continuation character (\).
"""

message = "Hello There.\nYou have come to the right place to learn Python"\
"Programming.\nFollow the tutorials to become expert in Python."\
"Don't forget to share it with your friends too."  # statement 4
 
math_result = 1 + 2 + 3 + 4 + \
              5 + 6 + 7 + 8 + \
              9 + 10  # statement 5
 
print(message)  # statement 6
print("Math Result :: "+str(math_result))  # statement 7

# 3. Multiple statements in a single line

"""
We can use semicolon (;) to have multiple statements in a single line.
"""

x = 1;y = 2;z = 3
print(x,y,z)
num=10;sum=num+10;print(sum)
