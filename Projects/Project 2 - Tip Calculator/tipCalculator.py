# Prerequisites of this project:
# 1. Create a greeting for your program.
# 2. Ask the user for total bill.
# 3. Ask the user for tip percentage (10, 12, or 15).
# 4. Ask the user for number of people.
# 5. Calculate the bill for each person including tip.

# Solution to this project:
print('Welcome to the Tip Calculator.')
totalBill = float(input("What was the total bill?\n$"))
tipPercentage = int(
    input("How much tip you would like to give in percentage?\n"))
noOfPeople = int(input('How many people to split the bill?\n'))
billWithTipPercentage = totalBill * tipPercentage
billWithTip = billWithTipPercentage / 100
finalBill = totalBill + billWithTip
individualBill = finalBill / noOfPeople
# 1st way minor advantage if bill is whole number, then only one decimal number
print(f'Each person should pay: ${round(individualBill, 2)}')
# 2nd way but every time 2 decimal points are displayed even bill is whole number
print(f'Each person should pay: $' + '{:.2f}'.format(individualBill))
print('Thank you for your cooperation.')
