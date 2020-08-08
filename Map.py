import math
import random
import pygame
import os

class Map():

    WIDTH = 800 # - 5
    HEIGHT = 800 # // 10
    GRID_SIZE = 16

    def __init__(self):
        self.map = [[GridSquare() for j in range(Map.WIDTH)]  for i in range(Map.HEIGHT)]

    def get_location(self, location):
        return self.map[location[0]][location[1]]

    def draw(self, win):
        for i in range(Map.WIDTH // Map.GRID_SIZE):
            for j in range(Map.WIDTH // Map.GRID_SIZE):
                terr = self.map[i][j].get_terrain()
                print(terr.get_image_path())
                win.blit(self.map[i][j].get_terrain().get_image_path(), (Map.GRID_SIZE * i, Map.GRID_SIZE * j))

    def __str__(self):
        output = ""
        for row in self.map:
            output += " ".join([gridSquare.get_terrain() for gridSquare in row])
            output += "\n"
        return output

    def _generate_struct(self, number_of_structs, terrain_id, min_count, max_count, threshold, count=0):
        for i in range(number_of_structs):
            initial_location = [random.randrange(0, Map.WIDTH // Map.GRID_SIZE), random.randrange(0, Map.HEIGHT // Map.GRID_SIZE)]
            self._grow_struct(initial_location, terrain_id, min_count, max_count, threshold)
            print(f"X: {initial_location[0]}, Y: {initial_location[1]}, ID: {terrain_id}")

    def _grow_struct(self, initial_location, terrain_id, min_count, max_count, threshold, count=0):
        count += 1
        surrounding_squares = []
        for i in [-2, -1, 0, 1, 2]:
            for j in [-2, -1, 0, 1, 2]:
                location = initial_location[:]
                location[0] += i
                location[1] += j
                square = self.get_location(location)
                terrain = square.get_terrain().get_id()
                if terrain not in [0, terrain_id]: return False

                if abs(i) < 2 and abs(j) < 2:
                    surrounding_squares.append((square, location))

        for square, location in surrounding_squares:
            if ( random.random() < threshold and count > min_count ) or count > max_count: continue
            square.set_terrain(terrain_id)
            if self._grow_struct(location, terrain_id, min_count, max_count, threshold,  count) == False: return
        return True

    def generate_valleys(self, valley_count=2):
        self._generate_struct(valley_count, 2, 2, 4, 0.8)

    def generate_lakes(self, lake_count=5):
        self._generate_struct(lake_count, 1, 5, 10, 0.94)

class GridSquare:

    def __init__(self, terrain_id=0):
        self.terrain = Terrain(terrain_id)

    def __str__(self):
        return self.terrain.get_name()

    def set_terrain(self, terrain_id):
        self.terrain = Terrain(terrain_id)

    def get_terrain(self):
        return self.terrain

class Terrain:

    TERRAIN_NAMES = ( "dirt", "water", "valley", "tree", "volcano" )
    # Could be individual elements instead of a 2d array
    # possiblity for random choice 
    TERRAIN_PATHS = (
            (pygame.image.load(os.path.join("Assets", "LightDirt.png"))), # Dirt
            (pygame.image.load(os.path.join("Assets", "LightWater.png"))), # Water
            (pygame.image.load(os.path.join("Assets", "Valley.png"))), # Valley
            (pygame.image.load(os.path.join("Assets", "Rabbit.png"))), # Tree
            (pygame.image.load(os.path.join("Assets", "foxidle1.png"))) # Volcano
#    pygame.image.load(os.path.join("Assets", "LightDirt.png")),
#    pygame.image.load(os.path.join("Assets", "DarkDirt.png")),
#    pygame.image.load(os.path.join("Assets", "LighGrass.png")),
#    pygame.image.load(os.path.join("Assets", "DarkGrass.png")),
#    pygame.image.load(os.path.join("Assets", "LightWater.png")),
#    pygame.image.load(os.path.join("Assets", "Valley.png")),
#    pygame.image.load(os.path.join("Assets", "Rabbit.png")),
#    pygame.image.load(os.path.join("Assets", "foxidle1.png"))
    )

    def __init__(self, terrain_id):
        self.terrain_id = terrain_id
        self.name = Terrain.TERRAIN_NAMES[terrain_id]
        self.image_path = Terrain.TERRAIN_PATHS[self.terrain_id]

    def get_name(self): return self.name
    def get_image_path(self): return self.image_path
    def get_id(self): return self.terrain_id

