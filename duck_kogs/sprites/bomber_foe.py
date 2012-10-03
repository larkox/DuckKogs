"""
Module that contains the BomberFoe class
"""
from duck_kogs import const
from duck_kogs.sprites import foe
from duck_kogs.sprites import bomb
from duck_kogs.sprites import bombs_group
import random


class BomberFoe(foe.Foe):
    """
    Defines the bomber Foe.
    This foe has an erratic movement, and sometimes, drops a bomb in the field.
    When hit, stops a few frames.
        pos = Initial position on the field
        sprite_img = texture where the sprite image is saved
    """
    def __init__(self, pos, game_map, sprite_img="bomberFoe.png"):
        super(BomberFoe, self).__init__(pos, game_map, sprite_img)

    def update(self, game_map):
        """
        Update the sprite
        """
        #TODO cuando recibe un golpe
        super(BomberFoe, self).update(game_map)
        self.frame_count += 1
        if self.frame_count == const.BOMBERSPEED:
            current_cell = self.get_current_cell(game_map)
            if random.random() < const.BOMBERMOVERATE:
                if self.move(
                    random.choice(current_cell.available_direction), game_map):
                    if random.random() < const.BOMBDROPRATE:
                        self.set_bomb(game_map, current_cell)
        self.frame_count %= const.BOMBERSPEED

    def set_bomb(self, game_map, cell):
        """
        Deploys a Bomb on its location.
        """
        bombs_group.BombsGroup().add(bomb.Bomb(cell.pos))
        pass
