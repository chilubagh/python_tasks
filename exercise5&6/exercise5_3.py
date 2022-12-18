# import pi from math
import math
# ask user for the radius of a circle
r = float(input('Enter the radius of a circle: '))
# calculate the radius of the circle
radius_of_circle = round(math.pi * r ** 2, 2)
print(f'Circle radius: {radius_of_circle}')
# ask if they want to continue using the program
while True:
    feedback = input('Do you want to continue? (y/n): ').lower()
    if feedback == 'y':
        r = float(input('Enter the radius of a circle: '))
        radius_of_circle = round(math.pi * r ** 2, 2)
        print(f'Circle radius: {radius_of_circle}')
    else:
        break

