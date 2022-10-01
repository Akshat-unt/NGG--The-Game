# Number guessing game

import random

def main():
    print_header()
    play_game()

def print_header():
    print('--------------------------------')
    print('        Number Guessing Game')
    print('--------------------------------')
    print()

def play_game():
    secret_number = random.randint(1, 100)
    guesses = []

    while True:
        guess = get_guess(guesses)
        guesses.append(guess)

        if guess < secret_number:
            print(f'Your guess of {guess} is too LOW.')
        elif guess > secret_number:
            print(f'Your guess of {guess} is too HIGH.')
        else:
            print(f'You got it! The number was {secret_number}')
            break

def get_guess(guesses):
    while True:
        guess_text = input('Guess a number between 1 and 100: ')
        try:
            guess = int(guess_text)
            if guess < 1 or guess > 100:
                print('Your guess must be between 1 and 100.')
            elif guess in guesses:
                print('You already guessed that number, silly.')
            else:
                return guess
        except ValueError:
            print('You must enter a number.')

if __name__ == '__main__':
    main()

# Number guessing game
