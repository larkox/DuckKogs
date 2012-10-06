"""
Module that contains the FastFoe class
"""
from duck_kogs.sprites import foe
from duck_kogs import const
from duck_kogs import signals
import random


class FastFoe(foe.Foe):
    """
    FastFoe
    """
    HEROPOS = None
    def __init__(self, pos, game_map, sprite_img="fastFoe.png"):
        super(FastFoe, self).__init__(pos, game_map, sprite_img)
        self.speed = const.SLOWFASTFOE

    def update(self, game_map):
        super(FastFoe, self).update(game_map)
        (direction, self.speed) = self.update_speed(game_map)
        if (self.frame_count > self.speed) and not self.moving:
            self.frame_count = 0
            if direction == const.FASTFOERANDOM:
                direction = random.choice(self.get_current_cell(
                    game_map).available_direction)
            if direction != const.FASTFOESTOP:
                self.move(direction, game_map)
        self.frame_count += 1

    def update_speed(self, game_map):
        """
        Calculate the speed an direction of the foe,
        regarding the player position
        """
        map_dimension = (game_map.width, game_map.height)
        if (FastFoe.HEROPOS == self.pos):
            return (const.FASTFOESTOP, const.FASTFASTFOE)
        if (FastFoe.HEROPOS[0] == self.pos[0]):
            choice_movement = [(0, 1), (0, -1)]
            choice_direction = [const.DOWN, const.UP]
            pos_index = 1
        elif (FastFoe.HEROPOS[1] == self.pos[1]):
            choice_movement = [(1, 0), (-1, 0)]
            choice_direction = [const.RIGHT, const.LEFT]
            pos_index = 0
        else:
            return (const.FASTFOERANDOM, const.SLOWFASTFOE)

        choice_lenght = [0, 0]
        if (FastFoe.HEROPOS[pos_index] > self.pos[pos_index]):
            choice_lenght[0] = FastFoe.HEROPOS[pos_index] - self.pos[pos_index]
            choice_lenght[1] = (self.pos[pos_index] + map_dimension[pos_index] -
                    FastFoe.HEROPOS[pos_index])
        else:
            choice_lenght[0] = (map_dimension[pos_index] - self.pos[pos_index] +
                    FastFoe.HEROPOS[pos_index])
            choice_lenght[1] = self.pos[pos_index] - FastFoe.HEROPOS[pos_index]
        step_count = [0, 0]
        reachable = [True, True]
        for i in range(2):
            for j in range(choice_lenght[i]):
                new_cell_pos = ((self.pos[0] + choice_movement[i][0] * j) %
                        map_dimension[0],
                        (self.pos[1] + choice_movement[i][1] * j) %
                        map_dimension[1])
                if not (choice_direction[i] in (game_map.get_cell(
                    new_cell_pos).available_direction)):
                    reachable[i] = False
                    break
            if reachable[i]:
                step_count[i] = j
        if not (reachable[0] or reachable[1]):
            return (-1, const.SLOWFASTFOE)
        elif (reachable[0] and reachable[1]):
            if (step_count[1] > step_count[0]):
                return (choice_direction[0], const.FASTFASTFOE)
            else:
                return (choice_direction[1], const.FASTFASTFOE)
        elif reachable[0]:
            return (choice_direction[0], const.FASTFASTFOE)
        else:
            return (choice_direction[1], const.FASTFASTFOE)



def handler(sender, pos, cells, **kwargs):
    """
    Handle the signal of the movement of the player
    """
    FastFoe.HEROPOS = pos

signals.PLAYER_MOVEMENT_SIGNAL.connect(handler)
