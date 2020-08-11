from Map import Map
from Location import Location
import pygame
import time
import os
import random
import math

from constants import *
from creatures import *

win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
clock = pygame.time.Clock()


gamerules = {
    "#Grass": 200,
    "#Rabbit": 20,
    "#Fox": 20,

    "#Water": 0,
    "#Valley": 0,

    "MaxGrass": 2000,
    "GrassDistance": 3
}


def spawnCreatures():
    while gamerules["#Grass"] > 0:
        gLocation = Location(random.randrange(SQUARECOUNT),
                             random.randrange(SQUARECOUNT))
        rLocation = Location(random.randrange(SQUARECOUNT),
                             random.randrange(SQUARECOUNT))
        fLocation = Location(random.randrange(SQUARECOUNT),
                             random.randrange(SQUARECOUNT))

        if gamerules["#Grass"] != 0 and Map.get_location(gLocation).get_terrain().get_id() == 0:
            Map.update(Grass(gLocation))
            gamerules["#Grass"] -= 1

        if gamerules["#Rabbit"] != 0 and Map.get_location(rLocation).get_terrain().get_id() == 0:
            Map.update(Rabbit(rLocation))
            gamerules["#Rabbit"] -= 1

        if gamerules["#Fox"] != 0 and Map.get_location(fLocation).get_terrain().get_id() == 0:
            Map.update(Fox(fLocation))
            gamerules["#Fox"] -= 1


def main():
    run = True

    # Map.create()
    Map.draw(win)

    spawnCreatures()

    while run:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run == False
                    pygame.quit()
                    quit()
        Map.iterate(win)
        pygame.display.update()


main()
