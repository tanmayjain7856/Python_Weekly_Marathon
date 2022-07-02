# Prerequisites of this project:
# 1. Create a greeting for your program.
# 2. Ask the user for option (rock, paper or scissors).
# 3. Set a random option for computer as well.
# 4. Based on both the options, declare a winner by comparing them.

# Solution to this project:
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userChoice = int(input(
    'What do you choose? Type 0 for Rock, 1 for paper or 2 for Scisors.\n'))
gameImages = [rock, paper, scissors]
choicesList = [0, 1, 2]
computerChoice = random.choice(choicesList)
if(userChoice < 3 and computerChoice < 3):
    print(f'\nYou chose: \n {gameImages[userChoice]}')
    print(f'Computer chose: \n {gameImages[computerChoice]}')
else:
    print('Invalid input')
if(userChoice == 0):
    if(computerChoice == 0):
        print('Draw')
    elif(computerChoice == 1):
        print('Computer wins')
    else:
        print('You win')
elif(userChoice == 1):
    if(computerChoice == 0):
        print('You win')
    elif(computerChoice == 1):
        print('Draw')
    else:
        print('Computer wins')
elif(userChoice == 2):
    if(computerChoice == 0):
        print('Computer win')
    elif(computerChoice == 1):
        print('You win')
    else:
        print('Draw')
else:
    print('Invalid Input')
