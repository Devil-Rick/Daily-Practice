import Data
import random as rn
import arts
import replit


def clear_screen():
    replit.clear()
    print(f"{arts.logo} \n\n")


def game(A, B):
    global score
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    A_value = A['follower_count']
    B_value = B['follower_count']
    win = False
    if (A_value > B_value and user_choice == "A") or ((A_value < B_value and user_choice == "B")):
        score += 1
        win = True
    return score, win


a = rn.randint(0, 49)
A = Data.data[a]
score = 0

correct = True
clear_screen()
try:
    while correct:
        b = rn.randint(0, 49)
        B = Data.data[b]
        if A != B:
            print(
                f"Compare A : {A['name']} , a {A['description']} , from {A['country']}.")
            print(arts.vs)
            print(
                f"\nCompare B : {B['name']} , a {B['description']} , from {B['country']}.\n")
            result = game(A, B)
            clear_screen()
            if result[1]:
                print(f"You're right! Current score: {result[0]} .\n")
                A = B
            else:
                correct = False
                print(f"Sorry, that's wrong. Final score: {result[0]}")
        else:
            continue
except:
    print("The Game Crashed ....\nKindly Restart the game.")
