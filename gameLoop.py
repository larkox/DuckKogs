import gameMap
from pygame.locals import *
import hero
import pygame
import foesGroup
import cogsGroup
import loop
import const
import sys


class GameLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self, mapName, textureName):
        #TODO anyadir bien y en el txt al personaje principal
        mapFile = open(mapName, 'r')
        self.gameMap = gameMap.GameMap(mapFile, textureName)
        self.cogs = cogsGroup.CogsGroup(self.gameMap)
        #TODO cambiar toda la iniciacion del heroe
        data = mapFile.readline().split(" ")
        self.hero = hero.Hero((int(data[0]), int(data[1])), self.gameMap)
        self.foes = foesGroup.FoesGroup(mapFile, self.gameMap)
        mapFile.close()

    def run(self, screen, clock):
        loopExit = False
        while not loopExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        self.hero.move(0, self.gameMap)
                    if event.key == K_RIGHT:
                        self.hero.move(1, self.gameMap)
                    if event.key == K_DOWN:
                        self.hero.move(2, self.gameMap)
                    if event.key == K_LEFT:
                        self.hero.move(3, self.gameMap)
            screen.blit(self.gameMap.mainSurface, (0, 0))
            #TODO recolocar el mapa
            self.cogs.update()
            self.foes.update(self.gameMap)
            self.cogs.draw(screen)
            self.foes.draw(screen)
            if self.hero.update(self.gameMap, self.cogs):
                loopExit = True
            if len(self.cogs) == 0:
                loopExit = True
            screen.blit(self.hero.image, self.hero.rect)
            pygame.display.flip()
            clock.tick(const.FPS)
