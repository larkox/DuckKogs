"""
Module that includes the DKGroups class
"""
import pygame


class DKGroups(pygame.sprite.Group, object):
    """
    Parent class from he sprite groups used in Duck Kogs game
    """
    def draw(self, surface):
        """
        Draws the sprites on the surface according the game map rectangle
        """
        for sprite in self.sprites():
            sprite.draw(surface)
