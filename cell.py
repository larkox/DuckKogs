import pygame
import const
class Cell:
    """
    Manages every cell on the game map.
        oFile: An oppened file with the map info, with the cursor on the
        beggining of a cell.
        pos: The position of the cell in the map.
        texture: The map texture surface.
        surface: The map surface, to draw the cell
    """
    def __init__(self,oFile,(posX,posY),texture,surface):
        #TODO pensar si hacen falta up down left right x y
        #We get if the direction is open or close
        self.up = int(oFile.read(1))
        self.down = int(oFile.read(1))
        self.left = int(oFile.read(1))
        self.right = int(oFile.read(1))
        #We get a list of available directions
        self.availableDirection = []
        if self.up:
            self.availableDirection.append(0)
        if self.right:
            self.availableDirection.append(1)
        if self.down:
            self.availableDirection.append(2)
        if self.left:
            self.availableDirection.append(3)
        oFile.read(1)
        #We get and write the chunk of the texture for this cell
        textPosX = (self.up + self.down*2)*const.SQUAREDIM
        textPosY = (self.left + self.right*2)*const.SQUAREDIM
        toDraw = texture.subsurface(((textPosX,textPosY),(const.SQUAREDIM,const.SQUAREDIM)))
        self.x = posX
        self.y = posY
        surface.blit(toDraw,(posX*const.SQUAREDIM,posY*const.SQUAREDIM))
        self.occupied = False
