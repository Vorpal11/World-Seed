from constants import *
from Location import *
from Map import Map
import random
class Creatures:

    def __init__(self, location):
        self.location = location

    def move(self, surroundings):
        direction = self.get_direction()
        if surroundings[direction] == []:
            return
        elif surroundings[direction].get_terrain().get_id() == 0:
            self.location = surroundings[direction].location

    def eat(self, creatureList):
        if self.id - 1 == creatureList[0].id:
            return creatureList[0]

    def reproduce(self):
        pass

    def draw(self, win):
        win.blit(self.IMG, self.location.get_coord_location())


class Rabbit(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.movesPerTurn = 1
        self.IMG = CREATURES[0]
        self.id = 1

    def get_direction(self):
        return random.randrange(0, 4)


class Fox(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.movesPerTurn = 2
        self.IMG = CREATURES[1]
        self.id = 2

    def get_direction(self):
        return random.randrange(0, 4)


class Grass(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.IMG = GRASS[random.randrange(0, 2)]
        self.id = 0

    def get_direction(self):
        return random.randrange(0, 4)

    def move(self, surroundings):
        pass

    def reproduce(self):
        pass
