import json


class GameMaster:

    def __init__(self):
        self.title = 'GameMaster'

    def prepareBoard(self):

        self.board = Board()
        self.board.preparePack()
        self.board.initGamers(self.number_of_gamers)



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
        self.cards = []
        self.cardsMap = {}
        self.firstId = 0
        data = {}
        with open('cards.txt') as json_file:
            data = json.load(json_file)
        for cardItem in data['cards']:
            card = Card(cardItem)
            self.cards.append(card)
            self.cardsMap[card.id] = card
            # print(str(card.tokens[0]))

    def nextCard(self):
        self.firstId = self.firstId + 1
        return self.cardsMap[self.firstId]

class Board:
    def __init__(self):
        self.title = 'Board'

    def preparePack(self):
        self.pack = Pack()
        return self.pack

    def setFirstCard(self, gamer):
        preCards = []
        x = range(1, 7)
        for n in x:
            card = self.pack.nextCard()
            preCards.append(card)
        print(preCards)

    def initGamers(self, number_of_gamers):
        self.gamers = []
        x = range(1, number_of_gamers + 1)
        for n in x:
            gamer = Gamer()
            gamer.id = n
            gamer.name = 'Gamer ' + str(gamer.id)
            self.gamers.append(gamer)
            self.setFirstCard(gamer)
            print(gamer.name)



class Gamer:
    def __init__(self):
        self.title = 'Gamer'


class Card:
    def __init__(self):
        self.title = 'Card'

    def __init__(self, cardItem):
        self.id = cardItem.get('id')
        self.tokens = cardItem.get('tokens')
        self.points = cardItem.get('points')
        self.type = cardItem.get('type')
        self.name = cardItem.get('name')
        self.region = cardItem.get('region')
        self.red = cardItem.get('red')
        self.gold = cardItem.get('gold')
        self.wheat = cardItem.get('wheat')
        self.action = cardItem.get('action')

        # "tokens":["sw", "sw", "st", "st", "da"],
        #"action":{"type": "remove", "what": "legions", "times": "all_from_one_card"}

class Token:
    def __init__(self):
        self.title = 'Token'


count = 1

gameMaster = GameMaster()
gameMaster.newGame()
