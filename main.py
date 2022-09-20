from hangman_art import stages
from hangman_art import logo
from hangman_words import word_lists
from hangman_art import sad
from hangman_art import smile
import random
import os

# word_list = []
# word_decision = int(
#     input(
#         "Would you like to use the in-built word list or create your own?\nType 1 to use in-built!\nType 2 to build your own!\nYour response: "
#     ))

# #word_list builder
# if word_decision == 1:
#     word_list = word_lists
# elif word_decision == 2:
#     word_list = input(
#         'Enter list of movies. Please separate them by a ",". Make sure no space (" ") after ",". Words can however have spaces between.(eg: Spider Man,Ant-man,batman):\n'
#     ).lower().split(',')
# else:
#     print("Invalid Resposnse, Exiting...")
#     exit()
# #List contents
# #print(word_list)
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# print(logo)
# #Testing code
# #print(f'The solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: \n").lower()
#     os.system('clear')

#     #Check if user entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#         print(f"You've already guessed {guess}")
  
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#             print(f"You have guessed {guess}. This is in the word! \n")

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         lives -= 1
#         print(
#             f"You have guessed {guess}. This is not in the word! You lose a life. Remaining lives: {lives}\n"
#         )
#         if lives == 0:
#             end_of_game = True
#             print("\nYou lose.\n")
#             print(sad)

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("\nYou win.\n")
#         print(smile)
#     #print hangman
#     print(stages[lives])

######################################################Version 2################################################################
#random movie picker
auto_picked_movie = random.choice(word_lists)
#print(auto_picked_movie) #uncomment this line if you want to see the movie name selected
movie=[]

#fills up spaces in "_" according to length of movie
for _ in range(len(auto_picked_movie)):
    movie += "_"
end_of_game = False
print(logo)
lives = 6
flag = False

#function compares guessed letter with word. if found, replaces in the correct indexes.
def guess(char,chosen_movie):
    for position in range(len(chosen_movie)):
        character = chosen_movie[position]
        if character == char and flag is False:
            movie[position] = char
            print(f"You have guessed {char}. This is in the word! \n")

    print(''.join(movie))

#while loop to continue running the game untill won or lost
while end_of_game is False:
    guess_char = input("Guess a letter: \n").lower()

    if guess_char in movie:
        flag = True
        print(f"You've already guessed {guess_char}")
    else:
        flag = False
    #function call
    guess(guess_char,auto_picked_movie)

    os.system('clear')
    
    #if "_" not found in movie list, instant win
    if "_" not in movie:
        end_of_game = True
        print("\nYou win.\n")
        print(smile)
    #if guessed letter not in chosen movie, lose a life and display art
    if guess_char not in auto_picked_movie:
        lives -= 1
        print(stages[lives])
        print(f"You have guessed {guess_char}. This is not in the word! Lives remaining: {lives}\n")
        if lives == 0:
            end_of_game = True
            print("\nYou lose.\n")
            print(sad)
