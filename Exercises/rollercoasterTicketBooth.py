print('Welcome to Rollercoaster!!!')
height = input('Enter your height in cm: ')
bill = 0
heightInCM = int(height)
if heightInCM >= 120:
    print('Yay!! You can ride the rollercoaster.')
    age = int(input('Enter your age: '))
    if age < 12:
        bill = 5
        print('Child tickets are $5.')
    if age <= 18:
        bill = 7
        print('Youth tickets are $7.')
    if age > 18:
        bill = 12
        print('Adult tickets are $12.')
    wantsPhoto = input('Do you want photos of yourself? Y or N. ')
    if wantsPhoto == 'Y':
        bill = bill + 3
    print(f'your final bill is ${bill}')
else:
    print("Sorry!! You can't ride the rollercoaster.")
