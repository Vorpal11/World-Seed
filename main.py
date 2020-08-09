from Map import Map
import pygame
import time
import os
import random
import math

from constants import ASSETS, WIDTH, HEIGHT, GRIDSIZE
from creatures import *
from grass import *

win = pygame.display.set_mode(
    (WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
clock = pygame.time.Clock()


def draw_window(win):
    for h in range(HEIGHT // GRIDSIZE):
        for w in range(WIDTH // GRIDSIZE):
            win.blit(ASSETS[0], (w * GRIDSIZE, h * GRIDSIZE))


def main():
    run = True
    rabbits = []
    foxs = []
    grasses = []
    grass_location = []
    for i in range(WIDTH // GRIDSIZE):
        rabbits.append(Rabbit(random.randrange(0, WIDTH // GRIDSIZE) *
                              GRIDSIZE, random.randrange(0, WIDTH // GRIDSIZE) * GRIDSIZE))
        foxs.append(Fox(random.randrange(0, WIDTH // GRIDSIZE) *
                        GRIDSIZE, random.randrange(0, WIDTH // GRIDSIZE) * GRIDSIZE))
        grasses.append(Grass(random.randrange(0, WIDTH // GRIDSIZE) *
                             GRIDSIZE, random.randrange(0, WIDTH // GRIDSIZE) * GRIDSIZE))
        grass_location.append((grasses[i].x, grasses[i].y))
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                pygame.quit()
                quit()
        draw_window(win)
        for grass in grasses:
            x, y = grass.reproduce(grass_location)
            if (x, y) != (-1, -1):
                grasses.append(Grass(x, y))
                grass_location.append((x, y))
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
