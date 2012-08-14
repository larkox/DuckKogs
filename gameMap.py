import pygame
import cell
import const
class GameMap:
    def __init__(self,mapFile,textureName="texture1.png"):
        #The texture is where all the celltypes are stored
        texture = pygame.image.load(textureName).convert()
        self.width = int(mapFile.readline())
        self.height = int(mapFile.readline())
        #The mainSurface is the surface which is gonna be blitted
        self.mainSurface = pygame.Surface((const.SQUAREDIM*self.width,const.SQUAREDIM*self.height))
        self.cells = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                line.append(cell.Cell(mapFile,(x,y),texture,self.mainSurface))
            self.cells.append(line)
