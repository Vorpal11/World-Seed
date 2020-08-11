import os
import pygame

GRIDSIZE = 16
SQUARECOUNT = 50

WIDTH = GRIDSIZE * SQUARECOUNT
HEIGHT = WIDTH

ASSETS = [
    pygame.image.load(os.path.join("Assets", "LightDirt.png")),
    pygame.image.load(os.path.join("Assets", "DarkDirt.png")),
    pygame.image.load(os.path.join("Assets", "LightWater.png")),
    pygame.image.load(os.path.join("Assets", "Valley.png")),
]
CREATURES = [
    pygame.image.load(os.path.join("Assets", "Rabbit.png")),
    pygame.image.load(os.path.join("Assets", "foxidle1.png"))
]

GRASS = [
    pygame.image.load(os.path.join("Assets", "LighGrass.png")),
    pygame.image.load(os.path.join("Assets", "DarkGrass.png")),
]
