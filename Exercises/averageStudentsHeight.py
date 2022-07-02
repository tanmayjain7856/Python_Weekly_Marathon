studentsHeight = input('Enter a list of student heights in cm.\n').split()
totalHeight = 0
numberOfStudents = 0
for height in studentsHeight:
    totalHeight += int(height)
    numberOfStudents += 1
averageHeight = totalHeight / numberOfStudents
print(f'Average height is: {round(averageHeight)}')
