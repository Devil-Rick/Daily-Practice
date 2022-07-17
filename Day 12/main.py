import replit
import random as rn
import game

play = True
try:
    while play:
        replit.clear()
        number = rn.randint(1, 101)
        print("Welcome to the number playing Game!!\n\n")
        print(
            "I'm thinking of a number between 1 and 100\nYou have to guess the number\n\n")
        difficulty = input(
            "Choose a difficulty level.\nType 'Easy' or 'Hard' : ").lower()
        print(game.play_game(difficulty, number))
        again = input(
            "Wanna play again ... If 'yes' press y otherwise 'no' : ").lower()
        if again == 'no':
            play = False

    print("Thank you for playing the game.")
except:
    print("Sorry Game Crashed.\nPlease restart the game...")
