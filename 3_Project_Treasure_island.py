print('Welcome to Treasure Island. Your mission is to find the treasure.')

direction = input('left or right?').lower()

if direction == 'left':
    swim_or_wait = input('swim or wait?').lower()
    if swim_or_wait == 'wait':
        door = input('Which door?').lower()
        if door == ('red'):
            print('Burned by fire. Game Over.')
        elif door == ('blue'):
            print('Eaten by beasts. Game Over.')
        elif door == ('yellow'):
            print('You Win!')
        else:
            print('Game over.')              
    else:
        print('Attacked by trout. Game Over.')
else:
    print('Fall into a hole. Game Over.')