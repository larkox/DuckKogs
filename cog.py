"""
Module that includes the Cog class
"""
import pygame
import const


class Cog(pygame.sprite.Sprite, object):
    """
    Includes the diferent cogs on the game.
    """
    def __init__(self, pos, texture="kog.png"):
        super(Cog, self).__init__()
        self.texture = pygame.image.load(texture)
        self.image = self.texture.subsurface(
                0, 0, const.SQUAREDIM, const.SQUAREDIM)
        self.pos = pos
        self.rect = pygame.Rect(pos[0] * const.SQUAREDIM,
            pos[1] * const.SQUAREDIM, const.SQUAREDIM, const.SQUAREDIM)
