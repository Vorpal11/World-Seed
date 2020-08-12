from constants import *
from Location import *
from Map import Map
import random
class Creatures:

    def __init__(self, location):
        self.location = location
        self.timeFood = 0

    def move(self, surroundings):
        if self.timeFood == 20:
            return False

        self.timeFood += 1

        direction = self.get_direction()
        if surroundings[direction] != [] and surroundings[direction].get_terrain().get_id() == 0:
            self.location = surroundings[direction].location
        return True

    def eat(self, creatureList):
        if self.id - 1 == creatureList[0].id:
            self.timeFood = 0
            return creatureList[0]

    def reproduce(self, surroundings):
        if self.timeFood == 0:
            for i in range(3):
                direction = random.randrange(0, 4)
                print(len(surroundings))
                if surroundings[direction] != [] and surroundings[direction].get_terrain().get_id() == 0:
                    Map.update(self.__class__(
                        surroundings[direction].location))
                    break

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
        return True

    def reproduce(self, surroundings):
        if random.random() > .96:
            if self.timeFood == 0:
                for i in range(2):
                    direction = random.randrange(0, 4)
                    if surroundings[direction] != [] and surroundings[direction].get_terrain().get_id() < 2:
                        Map.update(self.__class__(
                            surroundings[direction].location))
                        break
