import random
from art_blackjack import logo
print(logo)

computer_dealer = []
player = []

# computer_sum = 0
# player_sum = 0

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# global player_sum
# global computer_sum

# computer_sum = 0
# player_sum = 0



def play():

    computer_dealer.append(random.choice(cards))
    computer_dealer.append(random.choice(cards))

    player.append(random.choice(cards))
    player.append(random.choice(cards))

    player_sum = sum(player)
    computer_sum = sum(computer_dealer)

    print(f"Your cards: {player}, current score: {player_sum}.\nComputer's first card: {computer_dealer[0]}.")
    print(computer_dealer, computer_sum)
    print(computer_dealer, player)

    return player, computer_dealer

def runda(play):

    choice = input("Type 'y' to get another card, type 'n' or any other key to pass:\n")

    while choice == 'y':

        player.append(random.choice(cards))
        player_sum = sum(player)
    
    while computer_sum < 17:

        computer_dealer.append(random.choice(cards))
        computer_sum = sum(computer_dealer)

play()
runda(play)