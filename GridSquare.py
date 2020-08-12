from Location import Location
from Terrain import Terrain
import pygame
import os

# An object representing each cell on the map
# holding a creature and a terrain
class GridSquare:

    altered = []

    def __init__(self, location, terrain_id=0, sub_terrain_id=0):
        self.terrain = Terrain(terrain_id, sub_terrain_id)
        self.location = location
        self.creature_list = []
        GridSquare.altered.append(self)
        # print(len(GridSquare.altered))

    def draw(self, win):
        win.blit(self.terrain.get_image_path(),
                 self.location.get_coord_location())
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
        self.creature_list.sort(key=lambda x: x.id)

    # Remove a creature from the list of creatures currently on the square and
    # return true or false indicating if it was successful or not
    # TODO: Add and sort each time
    @set_altered
    def delete_creature(self, creature):
        if creature not in self.creature_list:
            return False
        self.creature_list.remove(creature)

    # Get the list of creatures currently on a sqaure
    def get_creature_list(self):
        return self.creature_list

    # Sets the terrain of the square to a new type using the terrainid
    def set_terrain(self, terrain_id, sub_terrain_id=0):
        if self.terrain.get_id() == terrain_id and self.get_terrain().get_sub_id() == sub_terrain_id:
            return
        self.terrain = Terrain(terrain_id, sub_terrain_id)

    # Gets the terrain item in the current square
    def get_terrain(self):
        return self.terrain
