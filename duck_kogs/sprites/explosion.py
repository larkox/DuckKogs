"""
Module that includes the Explosion class
"""
from duck_kogs.sprites import character
from duck_kogs import const


class Explosion(character.Character, object):
    """
    Includes the explosions on the game.
    """
    def __init__(self, pos, direction, game_map, texture="explosion.png"):
        super(Explosion, self).__init__(pos, texture)
        current_cell =  self.get_current_cell(game_map)
        if current_cell.occupied_by:
            current_cell.occupied_by.stun()
        self.get_current_cell(game_map).occupied = True

    def update(self, game_map):
        """
        Updates the state of the bomb
        """
        self.frame_count += 1
        if self.frame_count > const.EXPLOSIONTIME:
            self.get_current_cell(game_map).occupied = False
            self.kill()

    def move(self, direction, game_map):
        pass
