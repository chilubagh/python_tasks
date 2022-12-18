#  an applicaction that allows the user to calculate the statistics based on exam results.
 #  ask the user to enter the number of students in the class.test with small numbers.
students = int(input('Enter the number of students in the class: '))
total += exam_grades
 #  ask the user to enter the exams grades for each student in a loop.
for i in range(students):
#
    exam_grades= []
    total += exam_grades
    exam_grades.append(exam_grades)
    exam_grades = int(input('Enter the exam grades for each student. '))
    #print(f'Exam grades for each student: {exam_grades}')
    #  calculate the average grade for the class.
    average_grade = round(total_grades / students, 1)
    #  print the average grade for the class.
    print(f'The average grade for the class is {average_grade}.')
# calculate the median grade for the class.the middle number in th list
    print(sorted(exam_grades))
    median_grade = exam_grades[students // 2]
    print(f'The median grade for the class is {median_grade}.')
    print(f'The median grade for the class is {median_grade}.')
# calculate the mode grade for the class.the number that appears most in th list
    mode_grade = max(set(exam_grades), key=exam_grades.count)
    print(f'The mode grade for the class is {mode_grade}.')
#
#  print a text describing the average grade for the class.
if 0 <= average_grade < 1:
    print(f'Average grade: {average_grade}')
    print('Bad result')
elif 1 <= average_grade < 2:
    print(f'Average grad: {average_grade}')
    print('weak result')
elif 2 <= average_grade < 3:
    print(f'Average grad: {average_grade}')
    print('Average result')
elif 3 <= average_grade < 4:
    print(f'Average grad: {average_grade}')
    print('Good result')
else:
    print(f'Average grad: {average_grade}')
    print('Excellent result')