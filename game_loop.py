"""
Module that contains the GameLoop class
"""
import game_map
from pygame.locals import K_UP, K_RIGHT, K_LEFT, K_DOWN
import hero
import pygame
import foes_group
import cogs_group
import loop
import const
import sys


class GameLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self, map_name, texture_name):
        super(GameLoop, self).__init__()
        #TODO anyadir bien y en el txt al personaje principal
        map_file = open(map_name, 'r')
        self.game_map = game_map.GameMap(map_file, texture_name)
        self.game_map_rect = self.game_map.main_surface.get_rect()
        self.cogs = cogs_group.CogsGroup(self.game_map)
        #TODO cambiar toda la iniciacion del heroe
        data = map_file.readline().split(" ")
        self.hero = hero.Hero((int(data[0]), int(data[1])))
        self.foes = foes_group.FoesGroup(map_file, self.game_map)
        map_file.close()

    def run(self, screen, clock):
        loop_exit = False
        screen_rect = screen.get_rect()
        self.game_map_rect.center = screen_rect.center
        while not loop_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        self.hero.move(0, self.game_map)
                    if event.key == K_RIGHT:
                        self.hero.move(1, self.game_map)
                    if event.key == K_DOWN:
                        self.hero.move(2, self.game_map)
                    if event.key == K_LEFT:
                        self.hero.move(3, self.game_map)
            screen.blit(self.game_map.main_surface, self.game_map_rect)
            self.cogs.update()
            self.foes.update(self.game_map)
            self.cogs.draw(screen, self.game_map_rect)
            self.foes.draw(screen, self.game_map_rect)
            #TODO hacer las cosas bien con el eroe
            if self.hero.update(self.game_map, self.cogs):
                loop_exit = True
            if len(self.cogs) == 0:
                loop_exit = True
            new_rect = (
                    self.game_map_rect.left + self.hero.rect.left,
                    self.game_map_rect.top + self.hero.rect.top,
                    self.hero.rect.width,
                    self.hero.rect.height)
            screen.blit(self.hero.image, new_rect)
            pygame.display.flip()
            clock.tick(const.FPS)
