"""
Module that includes the class CreditsLoop
"""
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_LEFT, K_RIGHT
import pygame
from duck_kogs.loops import loop
from duck_kogs.loops import game_loop
from duck_kogs import const
import sys


class CreditsLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self):
        super(CreditsLoop, self).__init__()
        #TODO TEXTOS Y POSICIONES
        self.background = pygame.Surface((100, 150)).convert()
        self.background.fill((0, 255, 0))
        self.text = pygame.Surface((100, 150)).convert_alpha()
        self.render_text()

    def render_text(self):
        self.text.fill((0, 0, 0, 0))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("Design and development", True, (0, 0, 255))
        self.text.blit(text_img, (10, 10))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("Daniel Espino Garcia", True, (0, 0, 255))
        self.text.blit(text_img, (10, 30))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("Graphic design", True, (0, 0, 255))
        self.text.blit(text_img, (10, 50))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("Raquel Hernandez Toledo", True, (0, 0, 255))
        self.text.blit(text_img, (10, 70))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("Web", True, (0, 0, 255))
        self.text.blit(text_img, (10, 90))
        text = pygame.font.Font(const.FONT, 20)
        text_img = text.render("www.ducksanddreams.com", True, (0, 0, 255))
        self.text.blit(text_img, (10, 110))

    def run(self, screen, clock):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        return True
            screen.blit(self.background, (0, 0))
            screen.blit(self.text, (0, 0))
            pygame.display.flip()
            clock.tick(const.FPS)
