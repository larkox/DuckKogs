"""
Module that includes the Character class
"""
import pygame
from duck_kogs import const


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
        sprite_file = const.IMAGESDIR + sprite_img
        self.texture = pygame.image.load(sprite_file).convert_alpha()
        #TODO Arreglar para multiples sprites
        self.rect = pygame.Rect(
            (pos[0] * const.SQUAREDIM, pos[1] * const.SQUAREDIM),
            (const.SQUAREDIM, const.SQUAREDIM))
        self.image = self.texture.subsurface((0, 0),
                (const.SQUAREDIM, const.SQUAREDIM))
        self.moving = False
        self.frame_count = 0
        self.movement_speed = 30
        self.movement_frame_count = 0
        self.rect2 = self.rect.copy()
        self.double_blit = False




    Switch = {0: dir_up(),
            1: dir_right(),
            2: dir_down(),
            3: dir_left()}

    def move(self, direction, game_map):
        """
        Move the sprite in the given direction if possible.
        """
        if not self.moving:
            current_cell = self.get_current_cell(game_map)
            new_img_pos = (0,
                    (const.SQUAREDIM * direction) % self.texture.get_height())
            self.image = self.texture.subsurface(new_img_pos,
                    (const.SQUAREDIM, const.SQUAREDIM))
            if direction in current_cell.available_direction:
                self.moving = True
                self.prev_pos = self.pos
                movement = Character.Switch[direction]
                self.pos = (self.pos[0] + movement[0], self.pos[1] + movement[1])
                #We check if the character went form an edge to the other edge
                self.pos = (self.pos[0] % game_map.width,
                        self.pos[1] % game_map.height)
                #self.rect.topleft = (self.pos[0] * const.SQUAREDIM,
                    #self.pos[1] * const.SQUAREDIM)

    def update(self, game_map):
        super(Character, self).update()
        if self.moving:
            if self.movement_frame_count > self.movement_speed:
                self.finish_movement(game_map)
            elif (abs(self.pos[0] - self.prev_pos[0]) ==
                    game_map.height - 1):
                self.double_blit = True
                sign = ((self.pos[0] - self.prev_pos[0]) /
                        abs(self.pos[0] - self.prev_pos[0]))
                left = self.pos[1] * const.SQUAREDIM
                top1 = self.prev_pos[0] * const.SQUAREDIM
                top1 = top1 + (-sign * const.SQUAREDIM *
                        self.movement_frame_count) / self.movement_speed
                top2 = self.pos[0] * const.SQUAREDIM
                reverse_frame = self.movement_speed - self.movement_frame_count
                top2 = top2 + (sign * const.SQUAREDIM *
                        reverse_frame) / self.movement_speed
                self.rect.topleft = (top1, left)
                self.rect2.topleft = (top2, left)
                self.movement_frame_count += 1
            elif (abs(self.pos[1] - self.prev_pos[1]) ==
                    game_map.width - 1):
                self.double_blit = True
                sign = ((self.pos[1] - self.prev_pos[1]) /
                        abs(self.pos[1] - self.prev_pos[1]))
                top = self.pos[0] * const.SQUAREDIM
                left1 = self.prev_pos[1] * const.SQUAREDIM
                left1 = left1 + (-sign * const.SQUAREDIM *
                        self.movement_frame_count) / self.movement_speed
                left2 = self.pos[1] * const.SQUAREDIM
                reverse_frame = self.movement_speed - self.movement_frame_count
                left2 = left2 + (sign * const.SQUAREDIM *
                        reverse_frame) / self.movement_speed
                self.rect.topleft = (top, left1)
                self.rect2.topleft = (top, left2)
                self.movement_frame_count += 1
            else:
                top = self.pos[0] - self.prev_pos[0]
                top = top * const.SQUAREDIM
                top = (top * self.movement_frame_count) / self.movement_speed
                top = self.prev_pos[0] * const.SQUAREDIM + top
                left = self.pos[1] - self.prev_pos[1]
                left = left * const.SQUAREDIM
                left = (left * self.movement_frame_count) / self.movement_speed
                left = self.prev_pos[1] * const.SQUAREDIM + left
                self.rect.topleft = (top, left)
                self.movement_frame_count += 1

    def draw(self, surface):
        """
        Draws the character on a surface.
        """
        surface.blit(self.image, self.rect)
        if self.double_blit:
            surface.blit(self.image, self.rect2)
            self.double_blit = False

    def finish_movement(self, game_map):
        """
        Execute some actions after the movement is finished
        """
        self.moving = False
        self.rect.topleft = (self.pos[0] * const.SQUAREDIM,
                self.pos[1] * const.SQUAREDIM)
        self.movement_frame_count = 0

    def get_current_cell(self, game_map):
        """
        Get the current cell of the sprite on the game map
        """
        return game_map.get_cell(self.pos)
