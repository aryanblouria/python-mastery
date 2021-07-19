import pandas as pd
nato = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (index, row) in nato.iterrows()}

name = input("Enter your name: ")
phonetic_name = [phonetic_alphabet[letter.upper()] for letter in name]
print(phonetic_name)


