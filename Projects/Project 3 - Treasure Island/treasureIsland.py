# Prerequisites of this project:
# 1. Create a greeting for your program.
# 2. Ask the user for directions (left or right).
# 3. Based on direction given by user, move the user to another position.
# 4. Repeat above till the user finds the treasure or game is over.

# Solution to this project:
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')
direction = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right".\n').lower()
if direction == 'left':
    action = input(
        'You\'ve came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if action == 'wait':
        door = input(
            'You arrived at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose?\n').lower()
        if door == 'red':
            print('You burned by fire.\n!!!GAME OVER!!!')
        elif door == 'blue':
            print('You are eaten by beasts.\n!!!GAME OVER!!!')
        elif door == 'yellow':
            print('You found the treasure.\n!!!You win!!!')
        else:
            print('!!!GAME OVER!!!')
    else:
        print('You are attacked by piranhas.\n!!!GAME OVER!!!')
else:
    print('You fall into a hole.\n!!!GAME OVER!!!')
