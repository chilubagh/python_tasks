# create a list of cities
cities = ['Rome', 'Athens', 'Stockholm', 'London', 'Dublin', 'Paris' ]
# sorting the list
cities.sort()
# using for loop and printing thr row numbers using the index function
for city in cities:
    print(f'{cities.index(city) +1}: {city}')
