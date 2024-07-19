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
game_images = [rock, paper, scissors]

user_choice = int(input("Choose 0 for rock, 1 for paper, 2 for scissors:\n"))

computer_choice = random.randint(0, 2)

if (0 > user_choice or user_choice > 2):
    print("You typed wrong number!")
else:
    print("You chose:\n" + game_images[user_choice] + \
    "Computer chose:\n" + game_images[computer_choice])
    if (user_choice == computer_choice):
        print("Draw")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) \
    or (user_choice == 2 and computer_choice == 1):
        print("You won!")
    else:
        print("You lose")


