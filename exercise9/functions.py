# import math to get pi
import math
#  import random  for the lottery numbers
import random


# functions to print info on 3 different lines
def show_personal_info():
    print("John Williams")
    print("Rovaniemi")
    print("Cloud Data engineer")


# function to get total amount of seconds
def count_seconds(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds


# function to check serial number
def magazine_serial_check(serial):
    if serial[4] != "-":
        return False
    if len(serial) != 9:
        return False
    if not serial.replace("-", "").isdigit():
        return False
    else:
        return True


# functions to show numbered list
def show_numbered_list(title, data):
    print(title)
    for i, name in enumerate(data):
        print(f"{i + 1}. {name}")
    print()


# create 3 different functions for the volume
# volume of a box
def box_volume(width, height, depth):
    formula = width * height * depth
    formula = round(formula, 2)
    return formula


# volume of a ball
def ball_volume(radius):
    formula = (4 * math.pi * radius ** 3) / 3
    formula = round(formula, 2)
    return formula


# finding the volume of a pipe
def pipe_volume(radius, length):
    formula = (math.pi * radius ** 2 * length)
    formula = round(formula, 2)
    return formula


def lottery_numbers():
    # Generating a list of 7 unique numbers between 1 and 40
    number_drawn = random.sample(range(1, 41), 7)
    return number_drawn
