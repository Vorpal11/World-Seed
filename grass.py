import random
from constants import GRASS, GRIDSIZE, WIDTH, HEIGHT


class Grass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.IMG = GRASS[random.randrange(0, 2)]

    def reproduce(self, loc):
        directions = [0, 1, 2, 3]
        random.shuffle(directions)
        for dir in directions:
            if dir == 0 and self.x > 0 and (self.x - GRIDSIZE, self.y) not in loc:
                return (self.x - GRIDSIZE, self.y)

            elif dir == 1 and self.x < WIDTH - GRIDSIZE and (self.x + GRIDSIZE, self.y) not in loc:
                return (self.x + GRIDSIZE, self.y)

            elif dir == 2 and self.y > 0 and (self.x, self.y - GRIDSIZE) not in loc:
                return (self.x, self.y + GRIDSIZE)

            elif dir == 3 and self.y < HEIGHT - GRIDSIZE and (self.x, self.y + GRIDSIZE) not in loc:
                return (self.x, self.y - GRIDSIZE)

            else:
                directions.remove(dir)
            return (-1, -1)

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))
