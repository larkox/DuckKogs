"""
Module that includes the Bomb class
"""
from duck_kogs.sprites import character
from duck_kogs.sprites import explosions_group
from duck_kogs.sprites import explosion
from duck_kogs import const


class Bomb(character.Character, object):
    """
    Includes the bombs on the game.
    """
    SWITCH = {
            const.UP: (0, -1),
            const.RIGHT: (1, 0),
            const.DOWN: (0, 1),
            const.LEFT: (-1, 0)
            }
    def __init__(self, pos, texture="bomb.png"):
        super(Bomb, self).__init__(pos, texture)

    def update(self, game_map):
        """
        Updates the state of the bomb
        """
        self.frame_count += 1
        if self.frame_count > const.BOMBTIME:
            self.explode(game_map)
            self.kill()

    def move(self, direction, game_map):
        pass

    def explode(self, game_map):
        """
        Explodes the bomb
        """
        cell = self.get_current_cell(game_map)
        explosions_group.ExplosionsGroup().add(explosion.Explosion(
            self.pos, const.EXPLOSIONCENTER, game_map))
        for i in cell.available_direction:
            movement = Bomb.SWITCH[i]
            cell_location = ((self.pos[0] + movement[0]) % (game_map.width),
                    (self.pos[1] + movement[1]) % (game_map.height))
            explosions_group.ExplosionsGroup().add(explosion.Explosion(
                cell_location, i, game_map))
