"""
This module includes the Cell class
"""
import const


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
        #TODO pensar si hacen falta up down left right x y
        #We get if the direction is open or close
        open_up = int(o_file.read(1))
        open_down = int(o_file.read(1))
        open_left = int(o_file.read(1))
        open_right = int(o_file.read(1))
        #We get a list of available directions
        self.available_direction = []
        if open_up:
            self.available_direction.append(0)
        if open_right:
            self.available_direction.append(1)
        if open_down:
            self.available_direction.append(2)
        if open_left:
            self.available_direction.append(3)
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
        if text_pos_x + text_pos_y == 0:
            self.has_exit = False
        else:
            self.has_exit = True
