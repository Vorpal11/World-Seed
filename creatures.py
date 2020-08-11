from constants import ASSETS, CREATURES, WIDTH, HEIGHT, GRIDSIZE
class Creatures:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timeSinceFood = 0
        self.foodneeded = 2
        self.reproduced = 0

    def reproduce(self):
        if self.reproduced == 0 and foodneeded == 0:
            self.reproduced = 5
            return self.__class__(self.x, self.y)

    def move(self, dir):
        if self.reproduced <= 4:
            if dir == -2 and self.x > 0:
                #left (self.x - 1, self.y)
                self.x -= GRIDSIZE
            elif dir == -1 and self.x < WIDTH - GRIDSIZE:
                #right (self.x + 1, self.y)
                self.x += GRIDSIZE
            elif dir == 1 and self.y > 0:
                # up (self.x, self.y + 1)
                self.y -= GRIDSIZE
            elif dir == 2 and self.y < HEIGHT - GRIDSIZE:
                #Down (self.x, self.y - 1)
                self.y += GRIDSIZE

    def eat(self, creatureList):
        self.foodneeded = 2
        self.timeSinceFood = 0
        if creatureList[0].id == id - 1:
            return creatureList[0]

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
