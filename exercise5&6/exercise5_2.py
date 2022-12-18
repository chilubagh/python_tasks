# ask user for the amount of rain
# create a variable to store the total_rain
total_rain = 0
# use a for loop to ask the amount of rain 12 times in a year
for month in range(12):
    rain_amount = float(input('Enter the amount of rain for each month: '))
    total_rain = total_rain + rain_amount
    average_rain = round(total_rain / 12, 1)
    print(f'Year average for rain = {average_rain} mm')
