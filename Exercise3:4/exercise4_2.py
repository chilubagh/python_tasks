text1 = input('Enter a text: ')
# reverse the text
text2 = text1[::-1]
# checking if the text is the same as the reverse text
if text1 == text2:
    print(f'Palindrome: YES')
elif text1 != text2:
    print(f'Palindrome: NO')
# if an empty text is entered
else:
    print(f'Your text is empty')