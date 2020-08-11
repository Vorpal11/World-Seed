import pygame
import os

# An object representing each cell on the map
# holding a creature and a terrain
class GridSquare:

    altered = []

    def __init__(self, x, y, terrain_id=0):
        self.terrain = Terrain(terrain_id)
        self.x = x * 16
        self.y = y * 16
        self.creature_list = []
        GridSquare.altered.append(self)
        print(len(GridSquare.altered))

    def draw(self, win):
        win.blit(self.terrain.get_image_path(), (self.x, self.y))
        for creature in self.get_creature_list():
            creature.draw(win)

    # Return the name of the terrain currently in the square
    def __str__(self):
        return f"{self.__repr__()} : {len(self.creature_list)}"

#    def __repr__(self):
#        return ', '.join([str(c) for c in self.get_creature_list()])

    @staticmethod
    def reset_altered():
        altered = GridSquare.altered[:]
        GridSquare.altered = []
        return altered

    def set_altered(func):
        def inner(self, *args, **kwargs):
            if self not in GridSquare.altered:
                GridSquare.altered.append(self)
            return func(self, *args, **kwargs)
        return inner


    # Adds a creature to the list of cretures currently on the square
    @set_altered
    def add_creature(self, creature):
        self.creature_list.append(creature)

    # Remove a creature from the list of creatures currently on the square and
    # return true or false indicating if it was successful or not
    # TODO: Add and sort each time
    @set_altered
    def delete_creature(self, creature):
        if creature not in self.creature_list: return False
        self.creature_list.remove(creature)

    # Get the list of creatures currently on a sqaure
    def get_creature_list(self):
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


