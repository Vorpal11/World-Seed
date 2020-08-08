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

win = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
for i, x in enumerate(ASSETS):
    win.blit(x, (i * 16, 10))
pygame.display.update()

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
            pygame.quit()
            quit()
