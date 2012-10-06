"""
Module that includes the Hero class
"""
from duck_kogs.sprites import character
from duck_kogs import signals

class Hero(character.Character):
    """
    Builds and manages the hero sprite
    """
    def __init__(self, map_file, sprite_img="hero.png"):
        data = map_file.readline().split(" ")
        super(Hero, self).__init__((int(data[0]), int(data[1])), sprite_img)
        self.next_move = -1
        self.alive = True

    def update(self, game_map, cogs):
        """
        Update the hero sprite state
        """
        super(Hero, self).update(game_map)
        if not self.moving:
            if self.get_current_cell(game_map).occupied:
                self.alive = False
            cog = cogs.get_cog(self.pos)
            if cog != None:
                cog.kill()
        if self.next_move != -1:
            self.move(self.next_move, game_map)
            self.next_move = -1

    def move(self, direction, game_map):
        super(Hero, self).move(direction, game_map)
        signals.PLAYER_MOVEMENT_SIGNAL.send(
                self, pos = self.pos, cells = game_map.cells)
