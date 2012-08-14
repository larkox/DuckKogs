import pygame
import bomberFoe
import fastFoe
import angryFoe
import masterFoe

class FoesGroup(pygame.sprite.Group):
    """
    Group of Foes
    """
    def bomber():
        return bomberFoe.BomberFoe
    def fast():
        return fastFoe.FastFoe
    def angry():
        return angryFoe.AngryFoe
    def master():
        return masterFoe.MasterFoe
    Switch = {1: bomber(),
            2: fast(),
            3: angry(),
            4: master()}
    def __init__(self,mapFile):
        super(FoesGroup,self).__init__()
        for line in mapFile:
            #file format: Type PosX PosY
            data = line.split(" ")
            newSprite = FoesGroup.Switch[int(data[0])](
                    (int(data[1]),int(data[2])))
            self.add(newSprite)
    def update(self,gameMap):
        for foe in self.sprites():
            foe.update(gameMap)
