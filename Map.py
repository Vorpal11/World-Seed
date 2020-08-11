from Square import GridSquare
from constants import WIDTH, HEIGHT, GRIDSIZE, SQUARECOUNT
import math
import random
import pygame
import os

class Map:

    map = [[GridSquare(x, y) for x in range(WIDTH // GRIDSIZE)]
           for y in range(HEIGHT // GRIDSIZE)]

    @staticmethod
    def iterate(window):
        # I don't like this, resets too often
        Map.draw(window)
        # Move is a special function, we need to draw things moved
        # off of and onto, but only eat/repro on things moved onto
        Map.move()
        # Eat/repro shouldn't reset altered because theres no double iteration chance
        # assuming grass get switched around
        Map.eat()
        Map.reproduce()

    @staticmethod
    def move():
        #        Backup - set before iterating, through set when iterating should be the same
        #        altered = GridSquare.reset_altered()
        #        for gridSquare in altered:
        for gridSquare in GridSquare.reset_altered():
            print(gridSquare)
            creature_list = gridSquare.get_creature_list()
            for i, creature in enumerate(creature_list):
                x, y = creature.x // 16, creature.y // 16
                gridSquare.delete_creature(creature)
                print(creature)
                creature.move(Map.get_surrounding_squares(x, y))
                print(creature)
                Map.update(creature)

    @staticmethod
    def eat():
        for gridSquare in GridSquare.altered:
            creature_list = gridSquare.get_creature_list()[:]
            for creature in creature_list:
                eaten_creature = creature.eat(gridSquare.get_creature_list())
                if eaten_creature:
                    gridSquare.delete_creature(eaten_creature)

    # TODO: Can there be multiple things on the same square reproducing?
    # if len(creature_list) != 1: continue ?
    @staticmethod
    def reproduce():
        for gridSquare in GridSquare.altered:
            # Do we need to copy creature_list? besides (potentially) grass, there
            # shouldn't be anything that would be able to reproduce on the
            # same turn that it is created, right?
            creature_list = gridSquare.get_creature_list()[:]
            if len(creature_list) > 1:
                continue
            for creature in creature_list:
                creature.reproduce()

    @staticmethod
    def draw(window):
        for gridSquare in GridSquare.altered:
            gridSquare.draw(window)

    @staticmethod
    def update(creature_container):
        if not isinstance(creature_container, (list, tuple)):
            creature_container = [creature_container]
        for creature in creature_container:
            x = creature.x // 16
            y = creature.y // 16
            Map.map[y][x].add_creature(creature)

    @staticmethod
    def get_surrounding_squares(x, y):
        output = [[], [], [], []]
        if x > 0:
            output[0] = Map.get_location(x - 1, y).get_creature_list()
        if x < SQUARECOUNT - 1:
            output[1] = Map.get_location(x + 1, y).get_creature_list()
        if y > 0:
            output[2] = Map.get_location(x, y - 1).get_creature_list()
        if y > SQUARECOUNT - 1:
            output[3] = Map.get_location(x, y + 1).get_creature_list()
        return output

    @staticmethod
    def get_location(x, y):
        return Map.map[y][x]

    def __str__(self):
        output = ""
        for row in self.map:
            output += " ".join([gridSquare.get_terrain()
                                for gridSquare in row])
            output += "\n"
        return output

    # TODO: Recode these in a better/cleaner/more efficient way

    @staticmethod
    def generate_struct(number_of_structs, terrain_id, min_count, max_count, threshold, count=0):
        for i in range(number_of_structs):
            initial_location = [random.randrange(
                0, SQUARECOUNT), random.randrange(0, SQUARECOUNT)]
            Map.grow_struct(initial_location, terrain_id,
                            min_count, max_count, threshold)
            print(
                f"X: {initial_location[0]}, Y: {initial_location[1]}, ID: {terrain_id}")

    @staticmethod
    def grow_struct(initial_location, terrain_id, min_count, max_count, threshold, count=0):
        count += 1
        surrounding_squares = []
        # Check a 3x3 radius around the current square
        for i in [-2, -1, 0, 1, 2]:
            for j in [-2, -1, 0, 1, 2]:
                location = initial_location[:]
                location[0] += i
                location[1] += j
                square = Map.get_location(location[0], location[1])
                terrain = square.get_terrain().get_id()
                # If about to touch a different type of terrain, return
                if terrain not in [0, terrain_id]:
                    return False

                if abs(i) < 2 and abs(j) < 2:
                    # Add everything within a 2x2 area
                    surrounding_squares.append((square, location))

        # For each square within a 2x2 area
        for square, location in surrounding_squares:
            # Randomly skip, if about min count, or skip if above max count
            if (random.random() < threshold and count > min_count) or count > max_count:
                continue
            square.set_terrain(terrain_id)
            # Recursively grow for each block, and return false if it ends early
            if Map.grow_struct(location, terrain_id, min_count, max_count, threshold,  count) == False:
                return True
        return True

    # Generates valleys onto the map
    @staticmethod
    def generate_valleys(valley_count=2):
        Map.generate_struct(valley_count, 2, 2, 4, 0.8)

    # Generates lakes onto the map
    @staticmethod
    def generate_lakes(lake_count=5):
        Map.generate_struct(lake_count, 1, 5, 10, 0.94)

    @staticmethod
    def create():
        Map.generate_lakes()
        Map.generate_valleys()
