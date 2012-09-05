"""
Module that includes the Bomb class
"""
from duck_kogs.sprites import character
from duck_kogs import const


class Bomb(character.Character, object):
    """
    Includes the bombs on the game.
    """
    def __init__(self, pos, texture="bomb.png"):
        super(Bomb, self).__init__(pos, texture)

    def update(self, game_map):
    """
    Updates the state of the bomb
    """
        self.frame += 1
        if self.frame > const.FPS*3:
            self.get_current_cell(game_map).occupied = False
            self.kill()

    def move(self, direction, game_map):
        pass
