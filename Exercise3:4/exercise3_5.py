# ask the user the amounts of points and print the corresponding grade
amount_of_points = int(float(input("Enter the amount of points: ")))
# if the amount of points is less than 0 and  greater than 100, print grade point and the error message
if (amount_of_points < 0) or (amount_of_points > 100):
    print(f"Exam points: {amount_of_points} \nInvalid points value.")
# amount of points between 0-50, print grade 0
elif (amount_of_points >= 0) and (amount_of_points <= 50):
    print(f'Exams points: {amount_of_points} \nGrade: 0')
# if amounts of points entered 51-60
elif (amount_of_points >= 51) and (amount_of_points <= 60):
    print(f'Exam points:{amount_of_points} \nGrade: 1')
#if amounts of points entered 61-70
elif (amount_of_points >= 61) and (amount_of_points <= 70):
    print(f'Exam points: {amount_of_points} \nGrade: 2')
elif (amount_of_points >= 71) and (amount_of_points <= 80):
    print(f'Exam points: {amount_of_points} \nGrade: 3')
elif (amount_of_points >= 81) and (amount_of_points <= 90):
    print(f'Exam points: {amount_of_points} \nGrade: 4')
else:
    print(f'Exam points: {amount_of_points} \nGrade: 5')




