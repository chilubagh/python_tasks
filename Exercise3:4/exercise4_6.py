#ask for the current temperature and the humidity percentage.
current_temperature = int(input('Enter the current temperature: '))
humidity_percentage = int(input('Enter the humidity percentage: '))
#create also the follwoing boolean variables
freezing = False
heatwave = False
raining = False
hailstorm = False
#. if the current temperature is below 0, set the freezing variable to True,if the humidity percentage is above 80, set the raining  variable to True.if the current temperature is below -20, set the hailstorm variable to True.if the current temperature is over 20 set the heatwave variable tp true.above 80.
if (current_temperature) < 0:
    freezing = True
    print('Its freezing outside')
elif (humidity_percentage) > 80:
    raining = True
    print('Its raining outside')
elif (current_temperature) < -20:
    hailstorm = True
    print('Its hailstorm outside,becareful outside')
elif (current_temperature) > 20:
    heatwave = True
    print('Heatwave! Remember to hydrate')
else:
    print('Its damp and hot')
    