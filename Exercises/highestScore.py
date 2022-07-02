scores = input('Enter a list of student scores.\n').split()
highestScore = 0
for score in scores:
    if int(score) > highestScore:
        highestScore = int(score)
print(f'Highest score in class is: {highestScore}')
