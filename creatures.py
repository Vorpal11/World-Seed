from constants import *
from Location import *
class Creatures:

    def __init__(self, x, y):
        pass

    def reproduce(self):
        pass

    def move(self, dir):
        pass

    def eat(self, creatureList):
        pass

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))


class Rabbit(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.movesPerTurn = 1
        self.IMG = CREATURES[0]
        self.id = 1


class Fox(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.movesPerTurn = 2
        self.IMG = CREATURES[1]
        self.id = 2


class Grass(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.IMG = GRASS[random.randrange(0, 2)]
