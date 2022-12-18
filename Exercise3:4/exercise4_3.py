# save a text into a variable called text
text = 'The quick brown fox jumps over the lazy dog.That\ sentence contains every letters in the English alphabet.Neat!'
print(text)

# a) replace fox with duck. Use the replace() method

text1 = text.replace('fox', 'duck')
print(text1)
#ask the user for a word to be removed
word = input('Enter a word to be removed: ')
# if word is not in text variable
if word in text:
    text= text.replace(word, '')
    print(text)
else:
    print('word not found')

# printing the number of characters using the len()
numbers_of_characters = len(text)
print(f'The number of characters is : {numbers_of_characters}')

# counting the number of words using the split() and len()
words_count = text.split()
print(len(words_count))
# for text1
words_count1 = text1.split()
print(len(words_count1))

# dot and periods to new lines
text3 = text.replace('.', '')
print(text3)

# e) ask for a new sentence
usertext = input('Enter a new sentence: ')
if len(usertext) <= 20:
    print(usertext)
else:
    print

