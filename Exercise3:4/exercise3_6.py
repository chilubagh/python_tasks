
# checking for leap and not laep year
year = int(input('Enter a year of choice: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year: YES')
        else:
            print('Leap year:NO')
    else:
        print('leap year:YES')
else:
    print('Leap year:NO')