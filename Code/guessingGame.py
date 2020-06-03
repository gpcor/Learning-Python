import random
import sys
from time import sleep


class GuessingGame:
    name = ''
    guessCount = 0
    userGuess = ''
    userAnswer = ''

    def __init__(self):

        self.name = input('Hello, what is your name? ')
        print('Well {}, I am thinking of a number between 1 and 20. Can you guess it?'.format(
            self.name))
        print('You get 5 guesses, use them wisely!')
        sleep(2)

    def guessingGame(self):
        secretNumber = random.randint(1, 20)
        for self.guessCount in range(5):
            print('Take a guess!')
            try:
                self.userGuess = int(input())
                if self.userGuess > secretNumber:
                    print('That number is to high!')

                elif self.userGuess < secretNumber:
                    print('That number is too low!')

                elif self.userGuess == secretNumber:
                    print('That is the number!')
                    sleep(2)
                    break
            except KeyboardInterrupt:
                print('At least finsish the game, jeez...')
            except:
                if self.userGuess != int:
                    print('That is not a valid number...')
        else:
            print('You have ran out of guesses! The number I was thinking of was {}'.format(
                secretNumber))
            sleep(2)

    def newGameOrNah(self):
        print('Thanks for playing {}! Would you like to play again?'.format(self.name))
        while True:
            try:
                self.userAnswer = str.lower(input())
                if self.userAnswer == 'yes':
                    return self.userAnswer

                elif self.userAnswer != 'yes' and self.userAnswer != 'no':
                    print('It\'s a simple yes or no really. Do you want to play again?')
                else:
                    print('Bye {}!'.format(self.name))
                    sys.exit()
            except KeyboardInterrupt:
                print('So rude and abrupt...')
                sys.exit()


if __name__ == '__main__':
    game = GuessingGame()
    game.guessingGame()
    game.newGameOrNah()
    while True:
        if game.userAnswer == 'yes':
            game.guessingGame()
            game.newGameOrNah()
