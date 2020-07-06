import random
import sys
from time import sleep


class GuessingGame:
    name = ''
    guess_count = 0
    user_guess = ''
    user_answer = ''

    def __init__(self):

        self.name = input('Hello, what is your name? ')
        print('Well {}, I am thinking of a number between 1 and 20. Can you guess it?'.format(
            self.name))
        print('You get 5 guesses, use them wisely!')
        sleep(2)

    def guessing_game(self):
        secret_number = random.randint(1, 20)
        for self.guess_count in range(5):
            print('Take a guess!')
            try:
                self.user_guess = int(input())
                if self.user_guess > secret_number:
                    print('That number is to high!')

                elif self.user_guess < secret_number:
                    print('That number is too low!')

                elif self.user_guess == secret_number:
                    print('That is the number!')
                    sleep(2)
                    break
                elif self.user_guess != int:
                    print('That is not a valid number...')
            except KeyboardInterrupt:
                print('At least finsish the game, jeez...')

        else:
            print('You have ran out of guesses! The number I was thinking of was {}'.format(
                secret_number))
            sleep(2)

    def new_game_or_nah(self):
        print('Thanks for playing {}! Would you like to play again?'.format(self.name))
        while True:
            try:
                self.user_answer = str.lower(input())

                if self.user_answer != 'yes' and self.user_answer != 'no':
                    print('It\'s a simple yes or no really. Do you want to play again?')

                elif self.user_answer == 'yes':
                    return self.user_answer

                else:
                    print('Bye {}!'.format(self.name))
                    sys.exit()
            except KeyboardInterrupt:
                print('So rude and abrupt...')
                sys.exit()


if __name__ == '__main__':
    game = GuessingGame()
    game.guessing_game()
    game.new_game_or_nah()
    while True:
        if game.user_answer == 'yes':
            game.guessing_game()
            game.new_game_or_nah()
