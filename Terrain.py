from constants import TERRAIN
import pygame

class Terrain:
    # TODO: Make this into a list of constants to reduce the generation
    # and storage overhead

    # Sets a name and image path based on the given terrain id
    def __init__(self, terrain_id, sub_terrain_id=0):
        self.terrain_id = terrain_id
        self.sub_terrain_id = sub_terrain_id
        self.image_path = TERRAIN[self.terrain_id][self.sub_terrain_id]

    # Returns the terrains stringified name
    def get_name(self): return self.name
    # Returns the pygame image of the current terrain
    def get_image_path(self): return self.image_path
    # Returns the terrain id of the current square
    def get_id(self): return self.terrain_id



