import random


def playGame(p1, p2):
    if p1 == p2:
        print('Draw... Better Luck Next Time')
    if (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1):
        return 'Player 1'


def choices(in_choice):
    if in_choice == 0:
        return rock
    elif in_choice == 1:
        return paper
    elif in_choice == 2:
        return scissors
    else:
        return 'Invalid Input'


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


print('Simple "Rock" "Paper" "Scissor" Game')
game = int(input(
    'Want to Play against "Computer" or "Player". \nType 1 for "Computer" 2 for "Player " '))

if game == 1:
    p1 = int(
        input('What do you choose ? Type 0 for Rock , 1 for Paper , 2 for Scissor '))
    print(f'your choice \n {choices(p1)}')

    comp_choice = random.randint(0, 2)
    print(f'Computer Choice \n{choices(comp_choice)}')

    if playGame(p1, comp_choice) == 'Player 1':
        print('You are Damn Lucky....Congrats you have defeated the Computer..')
    else:
        print('You\'re luck Sucks ....You have lost against the Computer..')

elif game == 2:
    p1 = int(
        input('What do you choose PLayer 1? Type 0 for Rock , 1 for Paper , 2 for Scissor '))
    print(f'your choice \n {choices(p1)}')

    p2 = int(
        input('What do you choose Player 2? Type 0 for Rock , 1 for Paper , 2 for Scissor '))
    print(f'Computer Choice \n{choices(p2)}')

    if playGame(p1, p2) == 'Player 1':
        print(
            'You are way better than your opponent....Congrats you have defeated player 2..')
    else:
        print(
            'Looks like the opponent is better than YOU....You have lost against player 2..')
else:
    print('Invalid Input')
