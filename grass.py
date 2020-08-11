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
            if dir == 0 and self.x > 0:
                #left (self.x - 1, self.y)
                pass

            elif dir == 1 and self.x < WIDTH - GRIDSIZE:
                #right (self.x + 1, self.y)
                pass

            elif dir == 2 and self.y > 0:
                # up (self.x, self.y + 1)
                pass

            elif dir == 3 and self.y < HEIGHT - GRIDSIZE:
                #Down (self.x, self.y - 1)
                pass

            else:
                directions.remove(dir)

            return (-1, -1)

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))
