import random as r
import HangmanArts as ha
import HangmanWords as hw

print(ha.logo)
print('WELCOME to World of Hangman')
word = r.choice(hw.word_list)

try:
    word = word.upper()
    solution = list('_' for _ in range(0, len(word)))
    print("\n\n")
    print(" ".join(solution))
    print("\n\n\n")
    lives = 6
    while '_' in solution:
        if lives == 0:
            print("Game Over for you....Have a Better try next time")
            print(f"Answer : {word}")
            break
        else:
            userchar = input('Enter any alphabet : ').upper()
            for i in range(len(word)):
                if userchar == word[i]:
                    solution[i] = word[i]
                elif userchar not in word:
                    print(ha.stages[lives - 1])
                    lives -= 1
                    break
        print(" ".join(solution))
    if '_' not in solution and lives > 0:
        print("Congratulations you have completed the game")
except:
    print('Run again .... Server Error\nSorry the GAME Crashed')
