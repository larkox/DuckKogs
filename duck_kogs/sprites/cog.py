"""
Module that includes the Cog class
"""
from duck_kogs.sprites import character


class Cog(character.Character, object):
    """
    Includes the diferent cogs on the game.
    """
    def __init__(self, pos, texture="kog.png"):
        super(Cog, self).__init__(pos, texture)

    def move(self, direction, game_map):
        pass
