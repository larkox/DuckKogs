"""
Module that includes the class PauseLoop
"""
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_LEFT, K_RIGHT
import pygame
from duck_kogs.loops import loop
from duck_kogs import const
import sys


class PauseLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self):
        super(PauseLoop, self).__init__()
        self.text = pygame.Surface((100, 150)).convert_alpha()
        self.text.fill((0, 0, 0, 0))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("Pause", True, (0, 0, 255))
        self.text.blit(text_img, (10, 10))

    def run(self, screen, clock):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        return True
            screen.blit(self.text, (0, 0))
            pygame.display.flip()
            clock.tick(const.FPS)
