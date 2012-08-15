import pygame
import cog


class CogsGroup(pygame.sprite.Group):
    def __init__(self, gameMap):
        super(CogsGroup, self).__init__()
        for line in gameMap.cells:
            for cell in line:
                if cell.hasExit:
                    self.add(cog.Cog(cell.pos))

    def getCog(self, pos):
        for cog in self.sprites():
            if cog.pos == pos:
                return cog
        return None