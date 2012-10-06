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
from duck_kogs.loops import die_loop
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
            game_surface = pygame.Surface(self.game_map.main_surface[0].get_size()).convert_alpha()
            game_surface.fill((0,0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pressed = pygame.key.get_pressed()
            if pressed[K_UP]:
                self.hero.next_move = const.UP
            elif pressed[K_RIGHT]:
                self.hero.next_move = const.RIGHT
            elif pressed[K_DOWN]:
                self.hero.next_move = const.DOWN
            elif pressed[K_LEFT]:
                self.hero.next_move = const.LEFT
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
            self.cogs.update(self.game_map)
            self.foes.update(self.game_map)
            self.bombs.update(self.game_map)
            self.explosions.update(self.game_map)
            self.cogs.draw(game_surface)
            self.bombs.draw(game_surface)
            self.foes.draw(game_surface)
            self.explosions.draw(game_surface)
            self.hero.update(self.game_map, self.cogs)
            if not self.hero.alive:
                loop_exit = True
                exit_reason = const.EXITDIED
            elif len(self.cogs) == 0:
                loop_exit = True
                exit_reason = const.EXITWON
            self.hero.draw(game_surface)
            screen.blit(game_surface, self.game_map_rect)
            pygame.display.flip()
            clock.tick(const.FPS)
            time += 1/float(const.FPS)
            frame_count += 1
        die_loop.DieLoop().run(screen, clock)
        self.bombs.empty()
        self.explosions.empty()
        return exit_reason
