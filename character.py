import pygame
import const
class Character(pygame.sprite.Sprite):
    """
    Base class for all the characters (foes and allies).
        pos: the position of the character
        spriteImg: the file where the sprite image is stored
    """
    def __init__(self,pos,spriteImg):
        super(Character,self).__init__()
        self.pos = pos
        self.texture = pygame.image.load(spriteImg).convert_alpha()
        self.rect = pygame.Rect((pos[0]*const.SQUAREDIM,pos[1]*const.SQUAREDIM),
                (const.SQUAREDIM,const.SQUAREDIM))
        self.image = self.texture.subsurface((0,0),
                (const.SQUAREDIM,const.SQUAREDIM))
        self.frameCount = 0
    
    def up():
        return (0,-1)
    def down():
        return (0,1)
    def left():
        return (-1,0)
    def right():
        return (1,0)
    Switch = { 0: up(),
            1: right(),
            2: down(),
            3: left()}

    def move(self,direction,gamemap):
        currentCell = self.getCurrentCell(gamemap)
        if direction in currentCell.availableDirection:
            movement = Character.Switch[direction]
            aux = self.pos
            self.pos = (self.pos[0]+movement[0],self.pos[1]+movement[1])
            #We check if the character went form an edge to the other edge
            if self.pos[0] < 0:
                self.pos = (gamemap.width-1,self.pos[1])
            elif self.pos[0] == gamemap.width:
                self.pos = (0,self.pos[1])
            elif self.pos[1] < 0:
                self.pos = (self.pos[0],gamemap.height-1)
            elif self.pos[1] == gamemap.height:
                self.pos = (self.pos[0],0)
            newCell = self.getCurrentCell(gamemap)
            if newCell.occupied:
                self.pos = aux
            else:
                #We update the rect information
                currentCell.occupied = False
                newCell.occupied = True
                self.rect.topleft = (self.pos[0]*const.SQUAREDIM,self.pos[1]*const.SQUAREDIM)

    def getCurrentCell(self,gamemap):
        return gamemap.cells[self.pos[1]][self.pos[0]]
