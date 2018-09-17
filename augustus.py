import json
import random

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
        if (self.type == 'add' and self.what == 'round'):
            print('Start round #' + str(self.roundNum))
        if (self.type == 'add' and self.what == 'card'):
            print('Add card id:' + str(self.cardid) + ' to task list player #:' + str(self.playerid))
        if (self.type == 'remove' and self.what == 'card'):
            print('Remove card id:' + str(self.cardid) + ' to task list player #:' + str(self.playerid))

class Logger:

    def __init__(self):
        self.logRecords = []

    def logAddCardToPlayerTasks(self, player, card):
        logAddTask = LogRecord(self.logRecords)
        logAddTask.type = 'add'
        logAddTask.what = 'card'
        logAddTask.cardid = card.id
        logAddTask.playerid = player.id
        logAddTask.playername = player.name

    def logRemoveCardFromPlayerTasks(self, player, card):
        logAddTask = LogRecord(self.logRecords)
        logAddTask.type = 'remove'
        logAddTask.what = 'card'
        logAddTask.cardid = card.id
        logAddTask.playerid = player.id
        logAddTask.playername = player.name

    def logAddRound(self, number_of_round):
        logAddRound = LogRecord(self.logRecords)
        logAddRound.type = 'add'
        logAddRound.what = 'round'
        logAddRound.roundNum = number_of_round

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

    def printCurrentRoundRecords(self):
        print('print current round')


class GameMaster:

    def __init__(self):
        self.title = 'GameMaster'
        self.logger = Logger()
        self.roundCounter = 0

    def prepareBoard(self):

        self.logger.logAddRound(self.roundCounter)
        self.board = Board()
        self.board.logger = self.logger
        self.board.preparePack()
        self.initGamers(self.number_of_gamers, self.board)



    def startGame(self):
        self.round = 1
        z = 'continue'
        while self.round > 0:
            z = raw_input('Round ' + str(self.round) + ' $')
            if z == "stop":
                break
            if z == "next round":
                self.round = self.round + 14
            if z == "print all logs" or z == "pal":
                self.logger.printAllRecords()

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

    def setFirstCards(self, player):
        player.taskCards = []
        x = range(1, 7)
        for n in x:
            card = self.board.pack.nextCard()
            player.addCard(card)
        y = range(1, 4)
        for n in y:
            player.removeRandomCard()
        print(player.taskCards)

    def initGamers(self, number_of_gamers, board):
        self.gamers = []
        x = range(1, number_of_gamers + 1)
        for n in x:
            player = Gamer(self.logger)
            self.board.addPlayer(player)
            player.board = board
            player.id = n
            player.name = 'Gamer ' + str(player.id)
            self.gamers.append(player)
            self.logger.logAddPlayer(player)
            self.setFirstCards(player)
        self.logger.printAllRecords()

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
        return self.cards.pop()


class Board:

    def addPlayer(self, player):
        self.players.append(player)

    def __init__(self):
        self.players = []
        self.title = 'Board'

    def preparePack(self):
        self.pack = Pack()
        return self.pack



class Gamer:
    def __init__(self, logger):
        self.logger = logger
        self.title = 'Gamer'
        self.cards = {}
        self.taskCards = []

    def removeFirstCardById(self, id):
        for card in self.taskCards:
            if (card.id == id):
                self.taskCards.remove(card)

    def removeRandomCard(self):
        randomIndex = random.randrange(1, 1 + len(self.taskCards), 1)

        if (randomIndex < len(self.taskCards)):
            self.logger.logRemoveCardFromPlayerTasks(self, self.taskCards[randomIndex])
            del self.taskCards[randomIndex]

    def addCard(self, card):
        self.taskCards.append(card)
        self.logger.logAddCardToPlayerTasks(self, card)

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
