import json


class Action:
    def __init__(self):
        self.title = 'Action'

    def printOut(self):
        printResult = '\nAction number:' + str(self.number)
        printResult += '\ntype:' + self.type
        printResult += '\nwhat:' + self.what
        printResult += '\nname:' + self.name
        printResult += '\nplayerid:' + str(self.playerid)
        print(printResult)


class Round:
    def __init__(self):
        self.actions = []
        self.title = 'Round'

    def getNumber(self):
        return self.number

    # prepartion's actions
    def addGamerAction(self, player):
        addGamerAction = Action()
        addGamerAction.type = 'add'
        addGamerAction.what = 'player'
        addGamerAction.name = player.name
        addGamerAction.playerid = player.id
        addGamerAction.number = len(self.actions) + 1
        self.actions.append(addGamerAction)

    def printOut(self):
        print('Round number ' + str(self.number))
        for action in self.actions:
            action.printOut()


class LogRecord:
    def __init__(self, logRecords):
        self.title = 'logRecord'
        self.id = len(logRecords) + 1
        logRecords.append(self)

    def printOut(self):
        print('LogRecord id:' + str(self.id))
        if (self.type == 'add' and self.what == 'player'):
            print('Add player id:' + str(self.playerid) + ' name:' + str(self.playername))


class Logger:

    def __init__(self):
        self.logRecords = []

    def logAddPlayer(self, player):
        logAddPlayer = LogRecord(self.logRecords)
        logAddPlayer.type = 'add'
        logAddPlayer.what = 'player'
        logAddPlayer.playername = player.name
        logAddPlayer.playerid = player.id

    def printAllRecords(self):
        print('\nStart print all log records')
        for logRecord in self.logRecords:
            logRecord.printOut()
        print('End print all log records\n')


class LaterRemoveMe:
    def __init__(self):
        self.rounds = []
        self.title = 'Logger'

    def addPrepareRound(self):
        self.rounds = []
        round = Round()
        round.number = 0
        self.rounds.append(round)

    def addNewRound(self):
        round = Round()
        round.number = len(self.rounds) + 1
        self.rounds.append(round)

    def getCurrentRound(self):
        return self.rounds[len(self.rounds) - 1]

    def addGamerAction(self, player):
        self.getCurrentRound().addGamerAction(player)

    def printOutCurrentRound(self):
        self.getCurrentRound().printOut()

class GameMaster:

    def __init__(self):
        self.title = 'GameMaster'
        self.logger = Logger()

    def prepareBoard(self):


        self.board = Board()
        self.board.logger = self.logger
        self.board.preparePack()
        self.board.initGamers(self.number_of_gamers)



    def startGame(self):
        self.round = 1
        z = 'continue'
        while self.round > 0:
            z = raw_input('Round ' + str(self.round) + ' ')
            if z == "stop":
                break
            if z == "next round":
                self.round = self.round + 1

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
            gamer.logger = self.logger
            gamer.id = n
            gamer.name = 'Gamer ' + str(gamer.id)
            self.gamers.append(gamer)
            self.setFirstCard(gamer)
            self.logger.logAddPlayer(gamer)
        self.logger.printAllRecords()

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
        self.bonus = cardItem.get('bonus')
        self.feature = cardItem.get('feature')
        # "tokens":["sw", "sw", "st", "st", "da"],
        #"action":{"type": "remove", "what": "legions", "times": "all_from_one_card"}

class Token:
    def __init__(self):
        self.title = 'Token'


count = 1

gameMaster = GameMaster()
gameMaster.newGame()
