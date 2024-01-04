import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!= random_number:
        guess =int(input(f'guess a numner between 1 and {x}:  '))
        if guess < random_number:
            print('sorry,guess again.too low.')
        elif guess > random_number:
            print('sorry, guess again.too hight. ')
    print(f'yay, congrate.you guess the number {random_number} correctly')
guess(10)