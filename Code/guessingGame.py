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
        userGuess = input()
        try:
            if int(userGuess) > secretNumber:
                print('That number is to high!')

            elif int(userGuess) < secretNumber:
                print('That number is too low!')

            elif int(userGuess) == secretNumber:
                print('That is the number!')
                break
        except:
            if userGuess != int:
                print('That is not a valid number...')
    else:
        print('You have ran out of guesses, better luck next time')


guessingGame()

while True:
    print(f'Thanks for playing {name}! Would you like to play again?')
    userAnswer = input()

    if userAnswer.lower() == 'yes':
        guessingGame()

    else:
        print(f'Bye {name}!')
        sys.exit()
