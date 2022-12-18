# create an application that asks the user to choose a multiplication table in the range of 1 to 10.stop the application when the user enters 0.
user_input = int(input('Enter a number between 1 and 10: '))
# using a while loop print the multiplication table of the number chosen by the user.
while user_input != 0:
    for i in range(1, 11):
        print(f'{user_input} x {i} = {user_input * i}')
    user_input = int(input('Enter a number between 1 and 10: '))
# stop the application when the user enters 0.
    if user_input == 0:
        break
# if the user enters a number that is not in the range of 1 to 10, print an error message and ask the user to enter a number again.
    elif user_input < 1 or user_input > 10:
        print('wrong number format')