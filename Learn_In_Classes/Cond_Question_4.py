years= int(input('Enter  the year: '))

if (years%400==0) or (years%4==0 and years%100!=0):
    print('this is leap year')
else:
    print('this is not leap year')
