import character
class Foe(character.Character):
    """
    Any foe inherits from this class
    """
    def __init__(self,pos,gameMap,spriteImg):
        super(Foe,self).__init__(pos,gameMap,spriteImg)
        self.getCurrentCell(gameMap).occupied = True
    def move(self,direction,gameMap):
        cell = self.getCurrentCell(gameMap)
        pos = self.pos
        rect = self.rect.copy()
        super(Foe,self).move(direction,gameMap)
        newCell = self.getCurrentCell(gameMap)
        if newCell.occupied:
            self.pos = pos
            self.rect = rect
        else:
            cell.occupied = False
            newCell.occupied = True
