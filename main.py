from hangman_art import stages
from hangman_art import logo
from hangman_words import word_lists
from hangman_art import sad
from hangman_art import smile
import random
import os

word_list = []
word_decision = int(
    input(
        "Would you like to use the in-built word list or create your own?\nType 1 to use in-built!\nType 2 to build your own!\nYour response: "
    ))

#word_list builder
if word_decision == 1:
    word_list = word_lists
elif word_decision == 2:
    word_list = input(
        'Enter list of movies. Please separate them by a ",". Make sure no space (" ") after ",". Words can however have spaces between.(eg: Spider Man,Ant-man,batman):\n'
    ).lower().split(',')
else:
    print("Invalid Resposnse, Exiting...")
    exit()
#List contents
#print(word_list)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code
#print(f'The solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    os.system('clear')

    #Check if user entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
  
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"You have guessed {guess}. This is in the word! \n")

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(
            f"You have guessed {guess}. This is not in the word! You lose a life. Remaining lives: {lives}\n"
        )
        if lives == 0:
            end_of_game = True
            print("\nYou lose.\n")
            print(sad)

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.\n")
        print(smile)
    #print hangman
    print(stages[lives])
