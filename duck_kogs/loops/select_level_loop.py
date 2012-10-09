"""
Module that includes the class SelectLevelLoop
"""
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_LEFT, K_RIGHT
import pygame
from duck_kogs.loops import loop
from duck_kogs.loops import game_loop
from duck_kogs import const
import sys


class SelectLevelLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self, stages_list):
        super(SelectLevelLoop, self).__init__()
        #TODO TEXTOS Y POSICIONES
        self.background = pygame.Surface((100, 150)).convert()
        self.background.fill((0, 255, 0))
        self.text = pygame.Surface((100, 150)).convert_alpha()
        self.stages_list = stages_list
        if len(stages_list) > const.MAXSTAGESPPAGE:
            self.size = const.MAXSTAGESPPAGE
        else:
            self.size = len(stages_list)
        self.page = 0
        self.render_text()
        self.highlight = pygame.Surface((80, 20)).convert()
        self.highlight.fill((255, 0, 0))

    def render_text(self):
        self.text.fill((0, 0, 0, 0))
        low_index = self.page * const.MAXSTAGESPPAGE
        high_index = (self.page + 1) * const.MAXSTAGESPPAGE
        i = 0
        for stage in self.stages_list[low_index:high_index]:
            text = pygame.font.Font(const.FONT, 20)
            name = stage.split("/")[-1]
            text_img = text.render(name, True, (0, 0, 255))
            self.text.blit(text_img, (10, 10+20*i))
            i += 1
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("Exit", True, (0, 0, 255))
        self.text.blit(text_img, (10, 20*i))

    def run(self, screen, clock):
        result = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        result = (result - 1) % (self.size + 1)
                    if event.key == K_DOWN:
                        result = (result + 1) % (self.size + 1)
                    if event.key == K_LEFT:
                        self.page = (self.page + 1) % (
                                (len(self.stages_list) / const.MAXSTAGESPPAGE) + 1)
                        result = 0
                        self.render_text()
                    if event.key == K_RIGHT:
                        self.page = (self.page + 1) % (
                                (len(self.stages_list) / const.MAXSTAGESPPAGE) + 1)
                        result = 0
                        self.render_text()
                    if event.key == K_RETURN:
                        if result == self.size:
                            return True
                        else:
                            game_loop.GameLoop.LIVES = 0
                            index = self.page * const.MAXSTAGESPPAGE + result
                            game_loop.GameLoop(self.stages_list[index]).run(screen, clock)
            screen.blit(self.background, (0, 0))
            screen.blit(self.highlight, (10, 30 * result))
            screen.blit(self.text, (0, 0))
            pygame.display.flip()
            clock.tick(const.FPS)
