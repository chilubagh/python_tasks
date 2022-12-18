# months of the year as tuple
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
# ask user for number between 1 and 12
question = int(input('Enter a number of the month: '))
print(months[question -1])