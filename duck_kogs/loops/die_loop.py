"""
Module that includes the class MenuLoop
"""
from pygame.locals import K_RETURN
import pygame
from duck_kogs.loops import loop
from duck_kogs import const
import sys


class DieLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self):
        super(DieLoop, self).__init__()
        #TODO TEXTOS Y POSICIONES
        self.text = pygame.Surface((100, 40)).convert_alpha()
        self.text.fill((0, 0, 0, 0))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("New game", True, (0, 0, 255))
        self.text.blit(text_img, (10, 10))

    def run(self, screen, clock):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        return
            blit_pos = screen.get_rect().center
            blit_pos = (blit_pos[0] - self.text.get_width() / 2,
                    blit_pos[1] - self.text.get_height() / 2)
            screen.blit(self.text, blit_pos)
            pygame.display.flip()
            clock.tick(const.FPS)
