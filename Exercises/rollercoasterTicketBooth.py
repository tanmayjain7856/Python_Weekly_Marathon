print('Welcome to Rollercoaster!!!')
height = input('Enter your height in cm: ')
heightInCM = int(height)
if heightInCM >= 120:
    print('Yay!! You can ride the rollercoaster.')
    age = int(input('Enter your age: '))
    if age < 12:
        print('Your ticket price will be $5.')
    elif age <= 18:
        print('your ticket price will be $7.')
    else:
        print('your ticket price will be $12.')
else:
    print("Sorry!! You can't ride the rollercoaster.")
