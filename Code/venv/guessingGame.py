import random
import sys

print('Hello, what is your name?')
name = input()

secretNumber = random.randint(1, 20)
print(f'Well {name}, I am thinking of a number between 1 and 20. Can you guess it?')
print('You get 5 guesses, use them wisely!')


def guessingGame():
    for i in range(5):
        print('Take a guess!')
        try:
            userGuess = int(input())
            if userGuess > secretNumber:
                print('That number is to high!')

            elif userGuess < secretNumber:
                print('That number is too low!')

            elif userGuess == secretNumber:
                print('That is the number!')
                break
        except KeyboardInterrupt:
            print('At least finsish the game, jeez...')
        except:
            if userGuess != int:
                print('That is not a valid number...')
    else:
        print(
            f'You have ran out of guesses! The number I was thinking of was {secretNumber}')


guessingGame()

print(f'Thanks for playing {name}! Would you like to play again?')

while True:
    try:
        userAnswer = str.lower(input())
        if userAnswer == 'yes':
            guessingGame()

        elif userAnswer != 'yes' and userAnswer != 'no':
            print('It\'s a simple yes or no really. Do you want to play again?')
        else:
            print(f'Bye {name}!')
            sys.exit()
    except KeyboardInterrupt:
        print('So rude and abrupt...')
        sys.exit()
