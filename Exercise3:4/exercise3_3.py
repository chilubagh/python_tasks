# ask the user number of hours worked and their hourly rate
hours = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))
# if the hours are less than 40, print the total pay
if hours <= 40:
    print(f"weekly wage: {hours * hourly_rate}€")
# if the hours are more than 40, print the total pay with overtime.over time is 0.5 times the hourly rate
elif hours > 40:
    overtime = (hours - 40) * (hourly_rate * 0.5)
    total_overtime_pay = hours * hourly_rate + overtime
    print(f"weekly wage: {total_overtime_pay}€")
else:
    print("no overtime")
     