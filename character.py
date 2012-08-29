"""
Module that includes the Character class
"""
import pygame
import const


def dir_up():
    """ Switch Function. Return the movement when the direction is up. """
    return (0, -1)

def dir_down():
    """ Switch Function. Return the movement when the direction is down. """
    return (0, 1)

def dir_left():
    """ Switch Function. Return the movement when the direction is left. """
    return (-1, 0)

def dir_right():
    """ Switch Function. Return the movement when the direction is right. """
    return (1, 0)

class Character(pygame.sprite.Sprite, object):
    """
    Base class for all the characters (foes and allies).
        pos: the position of the character
        sprite_img: the file where the sprite image is stored
    """
    def __init__(self, pos, sprite_img):
        super(Character, self).__init__()
        self.pos = pos
        self.texture = pygame.image.load(sprite_img).convert_alpha()
        #TODO Arreglar para multiples sprites
        self.rect = pygame.Rect(
            (pos[0] * const.SQUAREDIM, pos[1] * const.SQUAREDIM),
            (const.SQUAREDIM, const.SQUAREDIM))
        self.image = self.texture.subsurface((0, 0),
                (const.SQUAREDIM, const.SQUAREDIM))
        self.frame_count = 0




    Switch = {0: dir_up(),
            1: dir_right(),
            2: dir_down(),
            3: dir_left()}

    def move(self, direction, game_map):
        """
        Move the sprite in the given direction if possible.
        """
        current_cell = self.get_current_cell(game_map)
        if direction in current_cell.available_direction:
            movement = Character.Switch[direction]
            self.pos = (self.pos[0] + movement[0], self.pos[1] + movement[1])
            #We check if the character went form an edge to the other edge
            if self.pos[0] < 0:
                self.pos = (game_map.width - 1, self.pos[1])
            elif self.pos[0] == game_map.width:
                self.pos = (0, self.pos[1])
            elif self.pos[1] < 0:
                self.pos = (self.pos[0], game_map.height - 1)
            elif self.pos[1] == game_map.height:
                self.pos = (self.pos[0], 0)
            self.rect.topleft = (self.pos[0] * const.SQUAREDIM,
                self.pos[1] * const.SQUAREDIM)

    def get_current_cell(self, game_map):
        """
        Get the current cell of the sprite on the game map
        """
        return game_map.cells[self.pos[1]][self.pos[0]]
