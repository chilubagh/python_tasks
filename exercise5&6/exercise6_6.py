# create an application that conatains a list called basket and add 5 items to the list.
basket = ['apple', 'banana', 'cherry', 'carrot', 'potato', 'tomato', 'cabbage']
 # ask the user for a word.After this the contents of the basket list on separate lines. using a loop.
ask_user = input('Enter a word: ')
for i in basket:
    print(i)
    # if the word is not the list print word not found and dont print the list.
    if ask_user not in basket:
        print('Word not found')
        continue
#if the user enter a number instead word,print the other items in the list.
    if ask_user.isnumeric():
        print(basket[1:])
    elif ask_user.isnumeric():
        print(basket[0], basket[2:])
    elif ask_user.isnumeric():
        print(basket[0], basket[1], basket[3:])
    elif ask_user.isnumeric():
        print(basket[0], basket[1], basket[2], basket[4])
    elif ask_user.isnumeric():
        print(basket[0], basket[1], basket[2], basket[3])



