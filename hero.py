"""
Module that includes the Hero class
"""
import character


class Hero(character.Character):
    """
    Builds and manages the hero sprite
    """
    def __init__(self, pos, sprite_img="hero.png"):
        super(Hero, self).__init__(pos, sprite_img)

    def update(self, game_map, cogs):
        """
        Update the hero sprite state
        """
        cog = cogs.get_cog(self.pos)
        if cog != None:
            cog.kill()
        if self.get_current_cell(game_map).occupied:
            return True
        else:
            return False
