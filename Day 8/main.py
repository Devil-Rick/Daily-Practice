# CEASER CIPHER
import logo
import Cipher as cp

print(logo)
print('\n\nEncode and Decode YOUR private texts\n')
try_again = True
while try_again:
    todo = input(
        "Type 'encode' to encode the text or 'decode' to decode the text :\n").lower()
    word = input("Enter the text :\n")
    ciphernum = int(input("Cipher by Enter a number :\n"))
    print(cp.cipher(word, todo, ciphernum))
    repeat = input(
        "Type 'yes' if you want to go again ..... Otherwise type'no'.. \n").lower()
    if repeat == 'no':
        print("Thank you .....See ya")
        try_again = False
