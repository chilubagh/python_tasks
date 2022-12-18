# caesars cipher formula c = (x-n)%26
# ask the user for a word
word = input('Enter a word: ')
# ask the user for a shift number
shift = int(input('Enter a shift number: '))
# transform the word according to the caesar cipher algorithm and print it out
word = word.lower()
for i in range(len(word)):
    if word[i] == ' ':
        print(' ', end='')
    else:
        print(chr(ord(word[i]) + shift), end='')
# create a variable to store the encrypted word
encrypted_word = ''
# print the encrypted word
print(encrypted_word)

