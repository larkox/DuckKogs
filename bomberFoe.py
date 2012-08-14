import character
import const
import pygame
import random
class BomberFoe(character.Character):
    """
    Defines the bomber Foe.
    This foe has an erratic movement, and sometimes, drops a bomb in the field.
    When hit, stops a few frames.
        pos = Initial position on the field
        spriteImg = texture where the sprite image is saved
    """
    def __init__(self,pos,spriteImg="bomberFoe.png"):
        super(BomberFoe,self).__init__(pos,spriteImg)

    def update(self,gamemap):
        #TODO cuando recibe un golpe
        #TODO cuando coloca una bomba
        #TODO gestionar colisiones
        self.frameCount += 1
        if self.frameCount == const.BOMBERSPEED:
            if random.random() > const.BOMBERMOVERATE:
                currentCell = self.getCurrentCell(gamemap)
                self.move(random.choice(currentCell.availableDirection),gamemap)
        self.frameCount %= const.BOMBERSPEED
    def setBomb(self,gamemap):
        #TODO no esta ni empezado
        currentCell = self.getCurrentCell(gamemap)
