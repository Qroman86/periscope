import json


class GameMaster:

    def __init__(self):
        self.title = 'GameMaster'

    def prepareBoard(self):

        data = {}
        with open('cards.txt') as json_file:
            data = json.load(json_file)

        self.board = Board()
        self.board.preparePack()

    def startGame(self):
        round = 1
        z = 'continue'
        while round > 0:
            z = raw_input('Round ' + str(round) + ' ')
            if z == "stop":
                break
            if z == "next round":
                round = round + 1

    def newGame(self):
        print('new game')
        print('Input number of gamers (2-4)')
        self.number_of_gamers = input()
        # ToDo write wrapper for exceptions

        self.prepareBoard()
        self.startGame()

    def loadGame(self):
        print('load game')

    def saveGame(self):
        print('save game')


class Pack:
    def __init__(self):
        self.title = 'The pack'


class Board:
    def __init__(self):
        self.title = 'Board'

    def preparePack(self):
        self.pack = Pack()
        return self.pack

class Gamer:
    def __init__(self, number, name):
        self.title = 'Gamer'


class Card:
    def __init__(self):
        self.title = 'Card'


class Token:
    def __init__(self):
        self.title = 'Token'


count = 1
for card in data['cards']:
    # print('Name: ' + card['name'] + ' count=' + str(count))
    count = count + 1


gameMaster = GameMaster()
gameMaster.newGame()
