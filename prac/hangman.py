import random
from words import words
import string

def  get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the list
    while '-' in words or '' in words:
        word = random.choice(words)

    return word.upper

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabets = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    user_letter = input('Guess a letter:  ').upper()
user_input= input('type something: ')
print(user_input) 