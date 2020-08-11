from Map import Map
import pygame
import time
import os
import random
import math

from constants import *
from creatures import *
from grass import *


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
        gx, gy = (random.randrange(SQUARECOUNT),
                  random.randrange(SQUARECOUNT))
        rx, ry = (random.randrange(SQUARECOUNT),
                  random.randrange(SQUARECOUNT))
        fx, fy = (random.randrange(SQUARECOUNT),
                  random.randrange(SQUARECOUNT))

        if gamerules["#Grass"] != 0 and Map.get_location(gx, gy).get_terrain().get_id() == 0:
            Map.update(Grass(gx, gy))
            gamerules["#Grass"] -= 1

        if gamerules["#Rabbit"] != 0 and Map.get_location(gx, gy).get_terrain().get_id() == 0:
            Map.update(Grass(rx, ry))
            gamerules["#Rabbit"] -= 1

        if gamerules["#Fox"] != 0 and Map.get_location(gx, gy).get_terrain().get_id() == 0:
            Map.update(Grass(fx, fy))
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
        pygame.display.update()


main()
