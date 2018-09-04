#
class GameMaster:
    def __init__(self):
        self.title = 'GameMaster'

    def preparePack(self):
        pack = Pack()
        return pack


class Pack:
    def __init__(self):
        self.title = 'The pack'


class Board:
    def __init__(self):
        self.title = 'Board'


class Gamer:
    def __init__(self):
        self.title = 'Gamer'


class Card:
    def __init__(self):
        self.title = 'Card'


class Token:
    def __init__(self):
        self.title = 'Token'


gameMaster = GameMaster()
pack = gameMaster.preparePack()
print(pack.title)
