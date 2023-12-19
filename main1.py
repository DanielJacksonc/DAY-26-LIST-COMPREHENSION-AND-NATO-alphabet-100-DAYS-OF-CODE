import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
nato = True
while nato:
    word = input("Enter a word :").upper()
    try:

        output = [phonetic_dic[letter]for letter in word]
        print(output)
        nato = False
    except:
        print("Sorry, only letters in the alphabet please")

""" we can also do it in another way. example below"""


def generate_phonetics():

    word = input("Enter a word :").upper()
    try:

        output = [phonetic_dic[letter] for letter in word]


    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetics()
    else:
        print(output)
generate_phonetics()
