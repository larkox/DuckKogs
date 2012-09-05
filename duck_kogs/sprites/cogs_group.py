"""
Module that includes the Cogs_group class
"""
from duck_kogs.sprites import cog
from duck_kogs.sprites import dk_groups


class CogsGroup(dk_groups.DKGroups):
    """
    Defines the cog group behaviour.
    """
    def __init__(self, game_map):
        super(CogsGroup, self).__init__()
        for line in game_map.cells:
            for cell in line:
                if cell.has_exit:
                    self.add(cog.Cog(cell.pos))

    def get_cog(self, pos):
        """
        Get the cog in a position
        """
        for cog_i in self.sprites():
            if cog_i.pos == pos:
                return cog_i
        return None
