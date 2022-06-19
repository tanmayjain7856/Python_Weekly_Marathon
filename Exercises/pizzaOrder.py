print('Welcome to  Python Pizza Deliveries!')
size = input('What size of pizza do you want? S, M ot L ')
add_pepperoni = input('Do you want pepperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')
bill = 0
if(size == 'S'):
    bill = 15
if(size == 'M'):
    bill = 20
if(size == 'L'):
    bill = 25
if add_pepperoni == 'Y':
    if(size == 'S'):
        bill = bill + 2
    else:
        bill = bill + 3
if extra_cheese == 'Y':
    bill = bill + 1
print(f'Your final bill is ${bill}.')
