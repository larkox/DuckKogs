import character
import const
import pygame
import random
class MasterFoe(character.Character):
    def __init__(self,pos,spriteImg="bomberFoe.png"):
        super(pos,spriteImg)

    def update(self,gamemap):
        if random.random() > 0.0:
            currentCell = self.getCurrentCell(gamemap)
            self.move(random.choice(currentCell.availableDirection),gamemap)
    def setBomb(self,gamemap):
        currentCell = self.getCurrentCell(gamemap)
