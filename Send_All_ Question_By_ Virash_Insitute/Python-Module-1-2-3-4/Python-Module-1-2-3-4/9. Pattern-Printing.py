print("First Number Pattern ")
for num in range(10):
    for i in range(num):
        print ('*',end=' ')
        """The print() function inserts a new line at the end, by default.
        In Python 2, it can be suppressed by putting ',' at the end.
        In Python 3, "end =' '" appends space instead of newline."""
    # new line after each row to display pattern correctly
    print("\n")

print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

print("Third Number Pattern")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(row, 0, -1):
        print(column,end=' ')
    print("")

