"""
Module that contains the GameLoop class
"""
from pygame.locals import K_UP, K_RIGHT, K_LEFT, K_DOWN
from duck_kogs.sprites import hero
import pygame
from duck_kogs import game_map
from duck_kogs.sprites import foes_group
from duck_kogs.sprites import cogs_group
from duck_kogs.sprites import bombs_group
from duck_kogs.sprites import explosions_group
from duck_kogs.loops import loop
from duck_kogs import const
from duck_kogs import signals
import sys


class GameLoop(loop.Loop):
    """
    The loop to play the game.
    """

    LIVES = 0

    def __init__(self, map_name):
        super(GameLoop, self).__init__()
        map_file = open(map_name, 'r')
        self.game_map = game_map.GameMap(map_file)
        self.game_map_rect = self.game_map.get_rect()
        self.cogs = cogs_group.CogsGroup(self.game_map)
        self.hero = hero.Hero(map_file)
        signals.PLAYER_MOVEMENT_SIGNAL.send(self.hero, pos = self.hero.pos,
                cells = self.game_map.cells)
        self.foes = foes_group.FoesGroup(map_file, self.game_map)
        self.bombs = bombs_group.BombsGroup()
        self.explosions = explosions_group.ExplosionsGroup()
        map_file.close()
        self.background = pygame.Surface((
            const.SCREENWIDTH, const.SCREENHEIGHT))
        img = pygame.image.load(const.LEFTPANELIMG).convert()
        self.background.blit(img, const.LEFTPANELPOS)
        img = pygame.image.load(const.CENTRALPANELIMG).convert()
        self.background.blit(img, const.CENTRALPANELPOS)
        img = pygame.image.load(const.RIGHTPANELIMG).convert()
        self.background.blit(img, const.RIGHTPANELPOS)
        # Flush the event logger
        pygame.event.get()

    def run(self, screen, clock):
        loop_exit = False
        time = 0.0
        screen_rect = screen.get_rect()
        self.game_map_rect.center = screen_rect.center
        map_frame_index = 0
        frame_count = 0
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
            #TODO Mejorar lo de usar imagenes en vez de fuentes
            screen.blit(
                    pygame.font.Font(const.FONT, 60).render(
                        "%.0f" % time, True, (0, 0, 255)),
                    (730,20))
            screen.blit(
                    pygame.font.Font(const.FONT, 60).render(
                        "%d" % len(self.cogs), True, (0, 0, 255)),
                    (10,20))
            screen.blit(
                    pygame.font.Font(const.FONT, 60).render(
                        "%d" % GameLoop.LIVES, True, (0, 0, 255)),
                    (10,100))
            if (frame_count >= const.MAPFRAMESWITCH):
                map_frame_index = (map_frame_index + 1) % self.game_map.frames
                frame_count = 0
            screen.blit(self.game_map.main_surface[map_frame_index], self.game_map_rect)
            self.cogs.update()
            self.foes.update(self.game_map)
            self.bombs.update(self.game_map)
            self.explosions.update(self.game_map)
            self.cogs.draw(screen, self.game_map_rect)
            self.bombs.draw(screen, self.game_map_rect)
            self.foes.draw(screen, self.game_map_rect)
            self.explosions.draw(screen, self.game_map_rect)
            if self.hero.update(self.game_map, self.cogs):
                loop_exit = True
                exit_reason = const.EXITDIED
            if len(self.cogs) == 0:
                loop_exit = True
                exit_reason = const.EXITWON
            self.hero.draw(screen, self.game_map_rect)
            pygame.display.flip()
            clock.tick(const.FPS)
            time += 1/float(const.FPS)
            frame_count += 1
        self.bombs.empty()
        self.explosions.empty()
        return exit_reason
