# the artist file will be opened with the reading mode

artist_file = open('artists.txt', 'r')
# print the file
for album in artist_file:
    arrow = u'\u290D'
    print(arrow + album)