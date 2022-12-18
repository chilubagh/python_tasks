# print the numbers 1-50 using while loop
# set number equals 1 and using the while loop
number = 1
while number <= 50:
    print(number)
    number += 1  # this takes number variable and adds 1 to it

# b.using the for loop to print 1-50 inclusive.This makes the range 1-51.
number_list = range(1, 51)
for each_number in number_list:
    print(each_number)

# c.finding the sum of range between 1 and 30
num = range(1, 31)
# Initializing the variable sum with zero
sum = 0
# Use a for loop to iterate from 1 to 30.
for x in num:
# add the number to the sum and print the value
    sum = sum + x
print(f'sum: {sum}')

#d. with for loop print the years 2005 and 2010
# creating an empty string
period = ''
years = range(2005, 2011)
#add a new year to the period variable
for year in years:
    period = period + str(year) +  ' '
# removing the dash by using substring
period = period[0:-1]
print(period)