import character
class Hero(character.Character):
    def __init__(self,pos,gameMap,spriteImg="hero.png"):
        super(Hero,self).__init__(pos,gameMap,spriteImg)
    def update(self,gameMap):
        if self.getCurrentCell(gameMap).occupied:
            return True
        else:
            return False
