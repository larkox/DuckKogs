"""
Module that includes the DKGroups class
"""
import pygame


class DKGroups(pygame.sprite.Group, object):
    """
    Parent class from he sprite groups used in Duck Kogs game
    """
    def draw(self, surface, game_map_rect):
        """
        Draws the sprites on the surface according the game map rectangle
        """
        for sprite in self.sprites():
            new_rect = pygame.Rect(
                game_map_rect.left + sprite.rect.left,
                game_map_rect.top + sprite.rect.top,
                sprite.rect.width, sprite.rect.height)
            surface.blit(sprite.image, new_rect)
