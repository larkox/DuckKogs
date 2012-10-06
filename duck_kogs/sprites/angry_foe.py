"""
Module that inclues the AngryFoe class
"""
from duck_kogs.sprites import foe
from duck_kogs import const
from duck_kogs import signals


class AngryFoe(foe.Foe):
    """
    Angry Foe
    """
    DESTINY = None
    POTENTIALFIELD = None
    SWITCH = {
        const.UP: (0, -1),
        const.RIGHT: (1, 0),
        const.DOWN: (0, 1),
        const.LEFT: (-1, 0)
    }
    def __init__(self, pos, game_map, sprite_img="angryFoe.png"):
        super(AngryFoe, self).__init__(pos, game_map, sprite_img)

    def update(self, game_map):
        super(AngryFoe, self).update(game_map)
        if self.frame_count == const.ANGRYSPEED:
            self.move(0, game_map)
            self.frame_count = 0
        else: self.frame_count += 1

    def move(self, direction, game_map):
        if AngryFoe.POTENTIALFIELD:
            current_cell = self.get_current_cell(game_map)
            movement_direction = -1
            minimum_potential = AngryFoe.POTENTIALFIELD[
                    self.pos[1]][self.pos[0]]
            for i in current_cell.available_direction:
                movement = AngryFoe.SWITCH[i]
                cell_location = ((self.pos[0] + movement[0]) %
                        (game_map.width),
                        (self.pos[1] + movement[1]) %
                        (game_map.height))
                if (AngryFoe.POTENTIALFIELD[
                        cell_location[1]][cell_location[0]] <
                        minimum_potential):
                    minimum_potential = AngryFoe.POTENTIALFIELD[
                            cell_location[1]][cell_location[0]]
                    movement_direction = i
            super(AngryFoe, self).move(movement_direction, game_map)


    @classmethod
    def recalculate(cls, cells):
        """
        Recalculate the potential field for the map.
        """
        AngryFoe.POTENTIALFIELD = []
        k = -1
        for i in cells:
            AngryFoe.POTENTIALFIELD.append([])
            k += 1
            for j in i:
                AngryFoe.POTENTIALFIELD[k].append(0)
        AngryFoe.POTENTIALFIELD[AngryFoe.DESTINY[1]][AngryFoe.DESTINY[0]] = 1
        AngryFoe.recalculate_rec(cells, AngryFoe.DESTINY)

    @classmethod
    def recalculate_rec(cls, cells, pos):
        """
        Recursive method for recalculation.
        """
        new_potential = AngryFoe.POTENTIALFIELD[pos[1]][pos[0]] + 1
        current_cell = cells[pos[1]][pos[0]]
        for i in current_cell.available_direction:
            movement = AngryFoe.SWITCH[i]
            cell_location = ((pos[0] + movement[0]) % (len(cells)),
                    (pos[1] + movement[1]) % (len(cells[0])))
            if (AngryFoe.POTENTIALFIELD[
                cell_location[1]][cell_location[0]] == 0 or
                    AngryFoe.POTENTIALFIELD[
                        cell_location[1]][cell_location[0]] > new_potential):
                AngryFoe.POTENTIALFIELD[
                        cell_location[1]][cell_location[0]] = new_potential
                AngryFoe.recalculate_rec(cells, cell_location)



def handler(sender, pos, cells, **kwargs):
    """
    Handle the player movement signal
    """
    AngryFoe.DESTINY = pos
    AngryFoe.recalculate(cells)

signals.PLAYER_MOVEMENT_SIGNAL.connect(handler)
