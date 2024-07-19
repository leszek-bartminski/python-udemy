import random
from art_blackjack import logo
print(logo)
global game_finished
game_finished = False
computer_dealer = []
player = []

# computer_sum = 0
# player_sum = 0

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# global player_sum
# global computer_sum

# computer_sum = 0
# player_sum = 0

def runda(computer_sum, player_sum, game_finished):


    choice = 'y'
    while choice == 'y' and game_finished == False:
        
        choice = input("Type 'y' to get another card, type 'n' or any other key to pass:\n")
        player.append(random.choice(cards))
        player_sum = sum(player)


        computer_dealer.append(random.choice(cards))
        computer_sum = sum(computer_dealer)

    return computer_sum, player_sum

def play():

    game_finished = False

    computer_dealer.append(random.choice(cards))
    computer_dealer.append(random.choice(cards))

    player.append(random.choice(cards))
    player.append(random.choice(cards))

    player_sum = sum(player)
    computer_sum = sum(computer_dealer)

    print(f"Your cards: {player}, current score: {player_sum}.\nComputer's first card: {computer_dealer[0]}.")
    print(computer_dealer, computer_sum)
    print(player, player_sum)


    # choice = input("Type 'y' to get another card, type 'n' or any other key to pass:\n")

    # if choice == 'y':

    #     player.append(random.choice(cards))
    #     player_sum = sum(player)
    #     computer_dealer.append(random.choice(cards))
    #     computer_sum = sum(computer_dealer)

    runda(computer_sum, player_sum, game_finished) 
    computer_win = (22 > computer_sum >= 17 and (player_sum < 17 or player_sum > 21))
    player_win = (22 > player_sum >= 17 and (computer_sum < 17 or computer_sum > 21))

    while (computer_win or player_win):
        if computer_win and not player_win:
            print(f"Computer wins: {computer_sum}. You lose: {player_sum}")
            game_finished = True
            break
        elif player_win and not computer_win:
            print(f"You win: {player_sum}. Computer's result: {computer_sum}")
            game_finished = True
            break
        elif (computer_sum == player_sum) and computer_sum >= 17 and player_sum >= 17:
            game_finished = True
            print("Draw!")
            break
        else:
            runda(computer_sum, player_sum)
            
            # if 22 > computer_sum >= 17 and (player_sum < 17 or player_sum > 21):
            #     print(f"Computer wins: {computer_sum}. You lose: {player_sum}")

    
    [a, b] = runda(computer_sum, game_finished)
    print("Test: ", a, b)
    # print(rundlista)
    # print(computer_sum, player_sum)
    # print(computer_dealer, player)         
    

play()
