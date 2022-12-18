#import from the functions file
from functions import *

# ask for the respective parameters
hours = int(input("Enter your hours:\n"))
minutes = int(input("Enter your minutes:\n"))
seconds = int(input("Enter seconds:\n"))

time = int(input(f"{hours}h {minutes}min {seconds}sec"))
# total amount of seconds
#total_seconds = hours * 3600 + minutes * 60 + seconds
# print total amount of seconds
print(f"{total_seconds} seconds in total.")