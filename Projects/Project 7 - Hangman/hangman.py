# Prerequisites of this project:
# 1. Randomly choose a word from the list and assign it to a variable.
# 2. Create a list with blanks as much as letters in randomly chosen word.
# 3. Create a variable which will keep track of lives.
# 4. Ask the user to guess a letter and assign it to another variable and make it lowercase.
# 5. Check if the guessed letter is one of the letters in choosen word.
# 6. If the letter is present in chosen word, then replace the blank in display with that letter at that position.
# 7. If the letter is not present, then decrement lives by 1.
# 8. Game over when lives is equal to 0 or word is completely guessed.

# Solution to this project:
import random
import hangmanArt
import hangmanWords

end_of_game = False
chosen_word = random.choice(hangmanWords.word_list)
word_length = len(chosen_word)
lives = 6
display = ['_'] * word_length

print(hangmanArt.logo)

while end_of_game == False:
    guessed_letter = input('Guess a letter: ').lower()

    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = letter

    if guessed_letter not in chosen_word:
        print(
            f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(f'The correct word was {chosen_word}.')
            end_of_game = True
            print('You lose.')

    print(' '.join(display))

    if display.count('_') == 0:
        end_of_game = True
        print('You win.')

    print(hangmanArt.stages[lives])
