# __name__ and __main__

# guess the number game

import random


def guess_the_number():
    if __name__ == '__main__':
        print('You\'re directly running this module.')
    number = random.randint(1, 10)
    print(number)

    guess = int(input('Enter number between 1 and 10: '))
    attempt = 0
    while number != guess:
        if guess > number:
            print('Guess lower')
            attempt += 1
        else:
            print('Guess higher')
            attempt += 1
        guess = int(input('Guess again: '))

    print('You won!')
