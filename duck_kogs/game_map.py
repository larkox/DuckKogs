"""
Module that includes the GameMap class
and Cell class
"""
import pygame
from duck_kogs import const


class Cell(object):
    """
    Manages every cell on the game map.
        o_file: An oppened file with the map info, with the cursor on the
        beggining of a cell.
        pos: The position of the cell in the map.
        texture: The map texture surface.
        surface: The map surface, to draw the cell
    """
    def __init__(self, o_file, (pos_x, pos_y), texture, surface):
        #We get if the direction is open or close
        open_up = int(o_file.read(1))
        open_down = int(o_file.read(1))
        open_left = int(o_file.read(1))
        open_right = int(o_file.read(1))
        #We get a list of available directions
        self.available_direction = []
        if open_up:
            self.available_direction.append(const.UP)
        if open_right:
            self.available_direction.append(const.RIGHT)
        if open_down:
            self.available_direction.append(const.DOWN)
        if open_left:
            self.available_direction.append(const.LEFT)
        o_file.read(1)
        #We get and write the chunk of the texture for this cell
        text_pos_x = (open_up + open_down * 2) * const.SQUAREDIM
        text_pos_y = (open_left + open_right * 2) * const.SQUAREDIM
        to_draw = texture.subsurface((
            (text_pos_x, text_pos_y), (const.SQUAREDIM, const.SQUAREDIM)))
        self.pos = (pos_x, pos_y)
        surface.blit(to_draw,
            (pos_x * const.SQUAREDIM, pos_y * const.SQUAREDIM))
        self.occupied = False
        self.occupied_by = None
        if text_pos_x + text_pos_y == 0:
            self.has_exit = False
        else:
            self.has_exit = True

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
                line.append(Cell(
                    map_file, (pos_x, pos_y), texture, self.main_surface))
            self.cells.append(line)
    def get_cell(self, pos):
        return self.cells[pos[1]][pos[0]]
