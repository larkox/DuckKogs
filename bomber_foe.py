"""
Module that contains the BomberFoe class
"""
import const
import foe
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

    def update(self, gamemap):
        """
        Update the sprite
        """
        #TODO cuando recibe un golpe
        #TODO cuando coloca una bomba
        #TODO gestionar colisiones
        self.frame_count += 1
        if self.frame_count == const.BOMBERSPEED:
            if random.random() > const.BOMBERMOVERATE:
                current_cell = self.get_current_cell(gamemap)
                self.move(
                    random.choice(current_cell.available_direction), gamemap)
        self.frame_count %= const.BOMBERSPEED

    def set_bomb(self, game_map):
        """
        Deploys a Bomb on its location.
        """
        #TODO no esta ni empezado
        pass
