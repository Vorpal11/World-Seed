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

    def move(self):
        altered_squares = GridSquare.altered[:]
        # Allow all creatures to move
        for gridSquare in altered_squares:
            for creature in gridSquare.get_creature_list()[:]:
                if type(creature) == 'wolf': creature.move()
                change = creature.move()
                if change == None: continue
                self.get_location(change).add_creature(creature)
                gridSquare.delete_creature(creature)
#        # Allow all creatures to eat their sub-creature
#        for gridSquare in altered_squares:
#            if gridSquare.get_creature_list() > 1:
#                for creature in gridSquare.get_creature_list():
#                    gridSquare.delete_creature( creature.eat(gridSquare.get_creature_list()) )
#        # Allow reproduction 
#        for gridSquare in altered_squares:
#            for creature in gridSquare.get_creature_list():
#                if type(gridSquare) == 'Grass': creature.reproduce()
#                else: gridSquare.add_creature( creature.reproduce() )

    GridSquare.altered = []

    def draw(self):
        for gridSquare in GridSquare.altered:
            for creature in gridSquare.get_creature_list():
                creature.draw()

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
        # Check a 3x3 radius around the current square
        for i in [-2, -1, 0, 1, 2]:
            for j in [-2, -1, 0, 1, 2]:
                location = initial_location[:]
                location[0] += i
                location[1] += j
                square = self.get_location(location)
                terrain = square.get_terrain().get_id()
                # If about to touch a different type of terrain, return
                if terrain not in [0, terrain_id]: return False

                if abs(i) < 2 and abs(j) < 2:
                    # Add everything within a 2x2 area
                    surrounding_squares.append((square, location))

        # For each square within a 2x2 area
        for square, location in surrounding_squares:
            # Randomly skip, if about min count, or skip if above max count
            if ( random.random() < threshold and count > min_count ) or count > max_count: continue
            square.set_terrain(terrain_id)
            # Recursively grow for each block, and return false if it ends early
            if self._grow_struct(location, terrain_id, min_count, max_count, threshold,  count) == False: return True
        return True

    # Generates valleys onto the map  
    def generate_valleys(self, valley_count=2):
        self._generate_struct(valley_count, 2, 2, 4, 0.8)

    # Generates lakes onto the map  
    def generate_lakes(self, lake_count=5):
        self._generate_struct(lake_count, 1, 5, 10, 0.94)

# An object representing each cell on the map
# holding a creature and a terrain
class GridSquare:

    altered = []

    def __init__(self, terrain_id=0):
        self.terrain = Terrain(terrain_id)
        self.creature_list = []

    # Return the name of the terrain currently in the square
    def __str__(self):
        return self.terrain.get_name()

    def set_altered(func):
        def inner(self, *args, **kwargs):
            if self not in GridSquare.altered: GridSquare.altered.append(self)
            return func(self, *args, **kwargs)
        return inner


    # Adds a creature to the list of cretures currently on the square
    @set_altered
    def add_creature(self, creature):
        self.creature_list.append(creature)

    # Remove a creature from the list of creatures currently on the square and
    # return true or false indicating if it was successful or not
    @set_altered
    def delete_creature(self, creature):
        if creature not in self.creature_list: return False
        del self.creature_list[creature]

    # Get the list of creatures currently on a sqaure
    def get_creature_list(self, creature):
        return self.creature_list


    # Sets the terrain of the square to a new type using the terrainid 
    def set_terrain(self, terrain_id):
        if self.terrain.get_id() == terrain_id: return
        self.terrain = Terrain(terrain_id)

    # Gets the terrain item in the current square
    def get_terrain(self):
        return self.terrain

class Terrain:
    # TODO: Make this into a list of constants to reduce the generation
    # and storage overhead

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

    # Sets a name and image path based on the given terrain id
    def __init__(self, terrain_id):
        self.terrain_id = terrain_id
        self.name = Terrain.TERRAIN_NAMES[terrain_id]
        self.image_path = Terrain.TERRAIN_PATHS[self.terrain_id]

    # Returns the terrains stringified name
    def get_name(self): return self.name
    # Returns the pygame image of the current terrain
    def get_image_path(self): return self.image_path
    # Returns the terrain id of the current square
    def get_id(self): return self.terrain_id

