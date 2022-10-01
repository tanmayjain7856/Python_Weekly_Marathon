# Prerequisites of this project:
# 1. Create a greeting for your program.
# 2. Create a function called 'encrypt' that takes the 'text' and 'shift' as input.
# 3. Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# 4. Create a different function called 'decrypt' that takes the 'text' and 'shift' as input.
# 5. Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alphabet by the shift amount and print the decrypted text.
# 6(a). Check if the user wanted to encrypt or decrypt the message by checking 'direction' variable.
# 7. Merge both encrypt and decrypt functions into one function called 'caesar'
# 6(b). Now just call the merged function and pass required arguments
# 8. Restart the program if user type 'yes'

# Solution to this project:
from caesarCipherArt import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    for char in start_text:
        if char in alphabet:
            char_position = alphabet.index(char)
            if direction == "encode":
                new_position = char_position + shift_amount
                while new_position > 25:
                    new_position = new_position - len(alphabet)
            elif direction == "decode":
                new_position = char_position - shift_amount
                while new_position < -26:
                    new_position = new_position + len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {direction}d text is: {end_text}.')


while should_continue:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print('Goodbye')
