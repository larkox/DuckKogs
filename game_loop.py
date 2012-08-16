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

    LIVES = 0

    def __init__(self, map_name, texture_name):
        super(GameLoop, self).__init__()
        map_file = open(map_name, 'r')
        self.game_map = game_map.GameMap(map_file, texture_name)
        self.game_map_rect = self.game_map.main_surface.get_rect()
        self.cogs = cogs_group.CogsGroup(self.game_map)
        self.hero = hero.Hero(map_file)
        self.foes = foes_group.FoesGroup(map_file, self.game_map)
        map_file.close()
        self.background = pygame.Surface((800, 450))
        img = pygame.image.load("leftPanel.png").convert()
        self.background.blit(img, (0, 0))
        img = pygame.image.load("centralPanel.png").convert()
        self.background.blit(img, (80, 0))
        img = pygame.image.load("rightPanel.png").convert()
        self.background.blit(img, (720, 0))

    def run(self, screen, clock):
        loop_exit = False
        time = 0.0
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
            screen.blit(self.background, (0, 0))
            screen.blit(
                    pygame.font.Font(None, 60).render(
                        "%.0f" % time, True, (0, 0, 255)),
                    (730,20))
            screen.blit(
                    pygame.font.Font(None, 60).render(
                        "%d" % len(self.cogs), True, (0, 0, 255)),
                    (10,20))
            screen.blit(
                    pygame.font.Font(None, 60).render(
                        "%d" % GameLoop.LIVES, True, (0, 0, 255)),
                    (10,100))
            screen.blit(self.game_map.main_surface, self.game_map_rect)
            self.cogs.update()
            self.foes.update(self.game_map)
            self.cogs.draw(screen, self.game_map_rect)
            self.foes.draw(screen, self.game_map_rect)
            #TODO hacer las cosas bien con el eroe
            if self.hero.update(self.game_map, self.cogs):
                loop_exit = True
                exit_reason = 0 #The hero died
            if len(self.cogs) == 0:
                loop_exit = True
                exit_reason = 1 #The hero won
            self.hero.draw(screen, self.game_map_rect)
            pygame.display.flip()
            clock.tick(const.FPS)
            time += 1/float(const.FPS)
        return exit_reason
