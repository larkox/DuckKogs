"""
Module that includes the GameMap class
"""
import pygame
import cell
import const


class GameMap:
    """
    Builds and store the game map
    """
    def __init__(self, map_file, texture_name="texture1.png"):
        #The texture is where all the celltypes are stored
        texture = pygame.image.load(texture_name).convert()
        self.width = int(map_file.readline())
        self.height = int(map_file.readline())
        #The main_surface is the surface which is gonna be blitted
        self.main_surface = pygame.Surface(
            (const.SQUAREDIM * self.width, const.SQUAREDIM * self.height))
        self.cells = []
        for pos_y in range(self.height):
            line = []
            for pos_x in range(self.width):
                line.append(cell.Cell(
                    map_file, (pos_x, pos_y), texture, self.main_surface))
            self.cells.append(line)
