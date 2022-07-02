# Prerequisites of this project:
# 1. Create a greeting for your program.
# 2. Ask the user for number of letters.
# 3. Ask the user for number of symbols.
# 4. Ask the user for number of numeric values.
# 5. Generate a random password which fulfills user inputs.

# Solution to this project:
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

user_letters = int(
    input("How many letters would you like in your password?\n"))
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

password = []
finalPassword = ''

for letter in range(1, (user_letters + 1)):
    password.append(random.choice(letters))

for symbol in range(1, (user_symbols + 1)):
    password.append(random.choice(symbols))

for number in range(1, (user_numbers + 1)):
    password.append(random.choice(numbers))

random.shuffle(password)
for keyword in password:
    finalPassword += keyword
print(f'Here is your password: {finalPassword}')
