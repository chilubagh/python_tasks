

# ask the user to input 5 positive integers in a loop
# using a loop print the biggest number .
user_input = int(input('Enter 5 positive integers: '))
biggest_number = 0
for i in range(4):
    user_input = int(input('Enter 5 positive integers. '))
    if user_input > biggest_number:
        biggest_number = user_input
print(f'The biggest number from user: {biggest_number}')










