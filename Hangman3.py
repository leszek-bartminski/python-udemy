#Step 3

import random
from hangman_words import word_list 
import hangman_art

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

death = 0
i = 0
show = False


while "_" in display:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            show = True            
            for i in display:                 
                display[position] = letter
                                    
            if "_" not in display:
                print("You win!")
                break                    


        if guess not in chosen_word:
            show = False
            death += 1
            print(stages[7-death])
            if death == 7:
                # i += 1
                # print(stages[7-i])
                # if i == 7:
                print("You lose!")
                break
            else:
                break

    if show == True:
         print(display)

    if death == 7:
        break        


     
    

# print("You win!")

