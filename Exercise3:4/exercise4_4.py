# ask for 2 different numbers

number1= int(input('Enter a number of your choice: '))
number2 = int(input('Enter a second number: '))
# divide number1 by number 2
result = number1 / number2
print(result)

# if user inputs a text
if type(number1) == str or type(number2) == str:
    print('Incorrect format')
# if the user divided by zero
elif number2 == 0:
    try:
        number1 / number2
    except ZeroDivisionError:
        print('Cannot divide by zero')
