import pygame
import time
import os
import random
import math

from constants import ASSETS, WIDTH, HEIGHT, GRIDSIZE, GRASS
from creatures import *
from grass import *

win = pygame.display.set_mode(
    (WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
clock = pygame.time.Clock()


def draw_window(win):
    for h in range(HEIGHT // GRIDSIZE):
        for w in range(WIDTH // GRIDSIZE):
            win.blit(GRASS[random.randrange(0, 2)],
                     (w * GRIDSIZE, h * GRIDSIZE))


def main():
    numGrass = 2500
    numRabbit = 20
    numFox = 20

    run = True
    rabbits = []
    foxs = []
    grasses = []
    grass_location = []
    for i in range(numRabbit):
        rabbits.append(Rabbit(random.randrange(0, WIDTH // GRIDSIZE) *
                              GRIDSIZE, random.randrange(0, WIDTH // GRIDSIZE) * GRIDSIZE))
    for i in range(numFox):
        foxs.append(Fox(random.randrange(0, WIDTH // GRIDSIZE) *
                        GRIDSIZE, random.randrange(0, WIDTH // GRIDSIZE) * GRIDSIZE))
    for i in range(numGrass):
        pass
        # grasses.append(Grass() *
        # GRIDSIZE, random.randrange(0, WIDTH // GRIDSIZE) * GRIDSIZE))
        # grasses.append(Grass(random.randrange(0, WIDTH // GRIDSIZE) *
        # GRIDSIZE, random.randrange(0, WIDTH // GRIDSIZE) * GRIDSIZE))
    while run:
        clock.tick(0.00000000000000000001)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                pygame.quit()
                quit()
        draw_window(win)
        for grass in grasses:
            grass.draw(win)

        for rabbit in rabbits:
            rabbit.move(random.randrange(-2, 3))
            rabbit.draw(win)

        for fox in foxs:
            fox.move(random.randrange(-2, 3))
            fox.draw(win)

        pygame.display.update()


main()
