import os
import pygame

GRIDSIZE = 16
SQUARECOUNT = 50

WIDTH = GRIDSIZE * SQUARECOUNT
HEIGHT = WIDTH

def load(file_name):
    return pygame.image.load(os.path.join("Assets", file_name))

TERRAIN = [
    [ load("LightDirt.png"), load("DarkDirt.png") ],
    [ load("LightWater.png"), load("DarkWater.png") ],
    [ load("Valley.png") ]
]
CREATURES = [
        load("Rabbit.png"),
        load("foxidle1.png")
]

GRASS = [
        load("LightGrass.png"),
        load("DarkGrass.png")
]
