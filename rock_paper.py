print('Welcome to the Rock Paper Scissors Game')
print('Here are the rules for the game')
print('Rock beats Scissor, Paper beats Scissors and paper beats Rock')

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
---.__(___)'''

print(rock)
# Getting the input of the user
images = [rock, paper, scissors]
user = int(input('What do you choose? Type 0 for Rock,1 for Paper,2 for scissors: \n'))

if 0 <= user < len(images):
    print(images[user])
else:
    print("Invalid Choice. Please enter a valid index within the range 0 to", len(images) - 1)

# Setting the computer to make a random choice between 0 and 2
comp_choice = random.randint(0,2)
print(comp_choice)
computer_choice = images[comp_choice]
print('Computer choose \n',computer_choice)

## Condition for when a User lost or not using the input of user and random choice of user
if comp_choice == user :
    print('It was a draw')
elif comp_choice ==0 and user ==2:
    print('You lost. Sorry 😞')
elif comp_choice == 1 and user == 0:
    print('You lost. Sorry 😞')
elif comp_choice ==  2 and user ==1:
    print('You lost. Sorry 😞')
elif user >=3:
    print('Your input was invalid')
else:
    print('YOU WON!!!🎉🎉🎉🎉')      

