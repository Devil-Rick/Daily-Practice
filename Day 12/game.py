import hints


def play(chance, number, n_hint):
    for _ in range(chance+1):
        guess = int(input("Make a guess : "))
        if guess == number:
            return "You won"
        elif chance == 0:
            return f"The correct answer is {number}"
        else:
            if guess > number:
                print("Too High\nGuess Again")
            elif guess < number:
                print("Too Low\nGuess Again")

            hint_used = hints.hint(number, n_hint)
            count = 0
            print(hint_used[0])
            if hint_used[1] == "yes":
                count += 1
                n_hint -= count

            print(
                f"You have {(chance -1) - _} attempts remaining to guess the number")


def play_game(difficulty, number):
    chances = 10
    n_hint = 3
    if difficulty == 'hard':
        chances = 5
        n_hint = 1
    print(f"\nYou have {chances} attempts remaining to guess the number")
    return play(chances, number, n_hint)
