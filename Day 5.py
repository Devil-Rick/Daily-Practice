import random as rn
print('WELCOME To PyPassword Generator')
letters = int(input('How many Letters in the Password ?\n'))
numbers = int(input('How many Numbers in the Password ?\n'))
special = int(input('How many Special Characters in the Password ?\n'))

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^']

total = letters + numbers + special
total_characters = list(range(0, total))
password = list(range(0, total))

for _ in range(total):
    next_place = rn.choice(total_characters)
    if _ < letters:
        password[next_place] = rn.choice(letters_list)
    elif _ > letters and _ < (letters + numbers):
        password[next_place] = rn.choice(numbers_list)
    else:
        password[next_place] = rn.choice(symbols_list)
    total_characters.remove(next_place)

print(''.join(password))
