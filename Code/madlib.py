# A Mad-Lib game
from time import sleep
import pprint


def madLib(exclamation, firstAdjective, secondAdjective, thirdAdjective, firstNoun, secondNoun, firstVerb, secondVerb, anActivity, songSuggestion, aHelpfulItem, yourName):
    madLib = (f'''When I heard you were getting married, I immediately thought {exclamation}! You are going to be the most {firstAdjective} bride EVER! Before the big day, be sure to {firstVerb} your {firstNoun} and {secondVerb} your {secondNoun}. If you need someone to {anActivity}, I'm your person. On your wedding day you should totally wear a(n) {secondAdjective} {thirdAdjective} dress, dance your first dance as husband and wife to the song {songSuggestion}, and bring lots of {aHelpfulItem} for all the tears. Good luck! Love Always, {yourName}.''')
    print(madLib)


def madLibAsker():
    print("Let's make a Mad-lib! This one is called \"Marriage Advice\"")
    sleep(2)
    print("I have a few questions so let's get started...")
    sleep(2)
    yourName = input('What is your name: ')
    exclamation = input('Give me an exclamation of some sort: ')
    firstAdjective = input('Give me an adjective: ')
    firstVerb = input('Give me a verb: ')
    firstNoun = input('Give me a noun or plural noun: ')
    secondVerb = input('Give me a second verb: ')
    secondNoun = input('Give me a second noun: ')
    anActivity = input('Give me an activity: ')
    secondAdjective = input('Give me a second adjective: ')
    thirdAdjective = input('Give me a third adjective: ')
    songSuggestion = input('Give me a song suggestion: ')
    aHelpfulItem = input('Give me an item you find helpful: ')
    print('Okay, give me a second to cook up your Mad-Lib...')
    sleep(5)
    print('Bingo! here it is!')
    sleep(1)
    madLib(exclamation, firstAdjective, secondAdjective, thirdAdjective, firstNoun,
           secondNoun, firstVerb, secondVerb, anActivity, songSuggestion, aHelpfulItem, yourName)


madLibAsker()
