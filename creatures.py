from constants import ASSETS, CREATURES, WIDTH, HEIGHT, GRIDSIZE
class Creatures:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timeSinceFood = 0
        self.foodneeded = 2
        self.reproduced = 0

    def reproduce(self, x, y):
        self.reproduced = 5

    def move(self, dir):
        if self.reproduced <= 4:
            if dir == -2 and self.x > 0:
                self.x -= 16
            elif dir == -1 and self.x < WIDTH - GRIDSIZE:
                self.x += 16
            elif dir == 1 and self.y > 0:
                self.y += 16
            elif dir == 2 and self.y < HEIGHT - GRIDSIZE:
                self.y -= 16
            return (self.x, self.y)

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))


class Rabbit(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.movesPerTurn = 1
        self.IMG = CREATURES[0]


class Fox(Creatures):
    def __init__(self, *args):
        Creatures.__init__(self, *args)
        self.movesPerTurn = 2
        self.IMG = CREATURES[1]
