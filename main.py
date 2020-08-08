from Map import Map
import pygame
import time
import os
import random

ASSETS = [
    pygame.image.load(os.path.join("Assets", "LightDirt.png")),
    pygame.image.load(os.path.join("Assets", "DarkDirt.png")),
    pygame.image.load(os.path.join("Assets", "LighGrass.png")),
    pygame.image.load(os.path.join("Assets", "DarkGrass.png")),
    pygame.image.load(os.path.join("Assets", "LightWater.png")),
    pygame.image.load(os.path.join("Assets", "Valley.png")),
    pygame.image.load(os.path.join("Assets", "Rabbit.png")),
    pygame.image.load(os.path.join("Assets", "foxidle1.png"))
]

map = Map()
map.generate_valleys()
map.generate_lakes()
win = pygame.display.set_mode((800, 800))
map.draw(win)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
