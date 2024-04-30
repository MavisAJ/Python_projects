print('Welcome YOU! Here is the Treasure Island')
print('Your mission here is to find the treasure and fun whilst we at it')
crossroads = input('You are at crossroad! Do you want to go left or right? : ').lower()
if crossroads == 'left':
    swim = input('Do you want to swim or wait? : ').lower()
    if swim == 'wait':
        print('Welcome to the next stage')
        door = input('Which door: red,blue or yellow? ').lower()
        if door == 'Yellow':
            print('You Winn!! Here is your treasure')
        elif door == 'red' or 'blue':
             print('Game Over! Sorry')
    else:
        print('Game Over!')
else:
    print("Game Over")


