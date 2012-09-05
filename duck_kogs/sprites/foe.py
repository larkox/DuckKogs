"""
Module that includes the Foe class
"""
import character


class Foe(character.Character):
    """
    Any foe inherits from this class
    """
    def __init__(self, pos, game_map, sprite_img):
        super(Foe, self).__init__(pos, sprite_img)
        self.get_current_cell(game_map).occupied = True

    def move(self, direction, game_map):
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
            new_cell.occupied = True
            return True
