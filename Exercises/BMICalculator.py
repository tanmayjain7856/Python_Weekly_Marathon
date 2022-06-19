height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')
bmi = round(int(weight) / (float(height) ** 2), 2)
if bmi < 18.5:
    print(f'Your BMI is {bmi} and you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi} and you are healthy.')
elif bmi < 30:
    print(f'Your BMI is {bmi} and you are overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi} and you are obese.')
else:
    print(f'Your BMI is {bmi} and you are clinically obese.')
