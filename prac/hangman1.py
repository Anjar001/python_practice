import random
from words import words

def hangman(words):
    word=random.choice(words)
    turn=5
    guessmade=""
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    while len(words)>0:
        main_word=""
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+" - "
        if main_word==words:
            print(main_word)
            print("you_won")
            break
        print("guess the words",main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turn=turn-1
        if turn == 0:
            print("you loose")
            break

name=input("Enter your name->:  ")
print("welcome",name, "!!")
print("----------------")
print('Try to guess the word in 5 attempt')
hangman(words)