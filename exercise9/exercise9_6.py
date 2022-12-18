# import from functions the random module and using the sample function
#
from random import sample
# creating a list
number_drawn = list(range(1, 40))
weekly_draw = sample(number_drawn, 7)
if number_drawn not in weekly_draw:
    print(weekly_draw)

