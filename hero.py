import character


class Hero(character.Character):
    def __init__(self, pos, gameMap, spriteImg="hero.png"):
        super(Hero, self).__init__(pos, gameMap, spriteImg)

    def update(self, gameMap, cogs):
        cog = cogs.getCog(self.pos)
        if cog != None:
            cog.kill()
        if self.getCurrentCell(gameMap).occupied:
            return True
        else:
            return False
