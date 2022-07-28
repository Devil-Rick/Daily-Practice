import pandas as pd

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
main_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Give a word : ").upper()
print([main_dict[letter] for letter in user if letter in main_dict.keys()])
