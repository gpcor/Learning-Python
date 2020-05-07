# A Mad-Lib game
from time import sleep


class MadLib:
    yourName = ''
    exclamation = ''
    firstAdjective = ''
    firstVerb = ''
    firstNoun = ''
    secondVerb = ''
    secondNoun = ''
    anActivity = ''
    secondAdjective = ''
    thirdAdjective = ''
    songSuggestion = ''
    aHelpfulItem = ''
    madLib = ''

    def __init__(self):
        pass

    def madLibAsker(self):
        print("Let's make a Mad-lib! This one is called \"Marriage Advice\"")
        sleep(2)
        print("I have a few questions so let's get started...")
        sleep(2)
        self.yourName = input('What is your name: ')
        self.exclamation = input('Give me an exclamation of some sort: ')
        self.firstAdjective = input('Give me an adjective: ')
        self.firstVerb = input('Give me a verb: ')
        self.firstNoun = input('Give me a noun or plural noun: ')
        self.secondVerb = input('Give me a second verb: ')
        self.secondNoun = input('Give me a second noun: ')
        self.anActivity = input('Give me an activity: ')
        self.secondAdjective = input('Give me a second adjective: ')
        self.thirdAdjective = input('Give me a third adjective: ')
        self.songSuggestion = input('Give me a song suggestion: ')
        self.aHelpfulItem = input('Give me an item you find helpful: ')
        print('Okay, give me a second to cook up your Mad-Lib...')
        sleep(5)
        print('Bingo! here it is!')
        sleep(1)

    def madLibBuilder(self):
        self.madLib = (f'''When I heard you were getting married, I immediately thought {self.exclamation}! You are going to be the most {self.firstAdjective} bride EVER! Before the big day, be sure to {self.firstVerb} your {self.firstNoun} and {self.secondVerb} your {self.secondNoun}. If you need someone to {self.anActivity}, I'm your person. On your wedding day you should totally wear a(n) {self.secondAdjective} {self.thirdAdjective} dress, dance your first dance as husband and wife to the song {self.songSuggestion}, and bring lots of {self.aHelpfulItem} for all the tears. Good luck! Love Always, {self.yourName}.''')
        print(self.madLib)


if __name__ == '__main__':
    ml = MadLib()
    ml.madLibAsker()
    ml.madLibBuilder()
