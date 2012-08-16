"""
Module that includes the Hero class
"""
import character


class Hero(character.Character):
    """
    Builds and manages the hero sprite
    """
    def __init__(self, map_file, sprite_img="hero.png"):
        data = map_file.readline().split(" ")
        super(Hero, self).__init__((int(data[0]), int(data[1])), sprite_img)

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
    def draw(self, surface, rect):
        """
        Draws the hero on a surface.
        """
        surface.blit(self.image, (rect.left + self.rect.left,
            rect.top + self.rect.top, self.rect.width, self.rect.height))
