import Arts as art
import replit
import game

cards = {"A": 11, "K": 10, "Q": 10, "J": 10,
         "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
         "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

play = input(
    "Do you want to play a game of 'BLACKJACK' type 'y' to continue or 'n' to close : ").lower()

play = 'y'
try:
    while play == 'y':
        replit.clear()
        print(f"{art.logo} \n\n")
        print(game.intial_cards(cards))
        next_card = input(
            "Type 'y' to get another card or 'n' to pass : ").lower()
        if next_card == 'y':
            print(game.second_card(cards))
            print(game.results(cards))
        else:
            print(game.show_hand(cards))
        play = input(
            "\n\nDo you want to play a game of 'BLACKJACK' type 'y' to continue or 'n' to close : ").lower()
except:
    print("System Eroor . Restart the game.\nSorry for the inconvience.")
