"""
Module that includes the Foe class
"""
from duck_kogs.sprites import character
from duck_kogs import const


class Foe(character.Character):
    """
    Any foe inherits from this class
    """
    def __init__(self, pos, game_map, sprite_img):
        super(Foe, self).__init__(pos, sprite_img)
        self.get_current_cell(game_map).occupied = True
        self.get_current_cell(game_map).occupied_by = self
        self.stun_frame_count = 0
        self.stunned = False

    def move(self, direction, game_map):
        if not self.stunned:
            cell = self.get_current_cell(game_map)
            pos = self.pos
            rect = self.rect.copy()
            super(Foe, self).move(direction, game_map)
            new_cell = self.get_current_cell(game_map)
            if new_cell.occupied:
                self.pos = pos
                self.rect = rect
                return False
            else:
                cell.occupied = False
                cell.occupied_by = None
                new_cell.occupied = True
                new_cell.occupied_by = self
                return True

    def update(self, game_map):
        """
        Updates the state of the foe
        """
        super(Foe, self).update(game_map)
        if self.stunned:
            self.stun_frame_count += 1
            if self.stun_frame_count == const.STUNTIME:
                self.stun_frame_count = 0
                self.stunned = False
                cell = self.get_current_cell(game_map)
                cell.occupied = True
                cell.occupied_by = self

    def stun(self):
        """
        Get a foe stunned
        """
        self.stun_frame_count = 0
        self.stunned = True
