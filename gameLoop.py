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
        self.gameMapRect = self.gameMap.mainSurface.get_rect()
        self.cogs = cogsGroup.CogsGroup(self.gameMap)
        #TODO cambiar toda la iniciacion del heroe
        data = mapFile.readline().split(" ")
        self.hero = hero.Hero((int(data[0]), int(data[1])), self.gameMap)
        self.foes = foesGroup.FoesGroup(mapFile, self.gameMap)
        mapFile.close()

    def run(self, screen, clock):
        loopExit = False
        screenRect = screen.get_rect()
        self.gameMapRect.center = screenRect.center
        print self.gameMapRect
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
            screen.blit(self.gameMap.mainSurface, self.gameMapRect)
            self.cogs.update()
            self.foes.update(self.gameMap)
            self.cogs.draw(screen, self.gameMapRect)
            self.foes.draw(screen, self.gameMapRect)
            #TODO hacer las cosas bien con el eroe
            if self.hero.update(self.gameMap, self.cogs):
                loopExit = True
            if len(self.cogs) == 0:
                loopExit = True
            newRect = (
                    self.gameMapRect.left + self.hero.rect.left,
                    self.gameMapRect.top + self.hero.rect.top,
                    self.hero.rect.width,
                    self.hero.rect.height)
            screen.blit(self.hero.image, newRect)
            pygame.display.flip()
            clock.tick(const.FPS)
