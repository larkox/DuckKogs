from pygame.locals import *
import pygame
import loop
import const
import sys


class MenuLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self):
        self.background = pygame.Surface((100, 150)).convert()
        self.background.fill((0, 255, 0))
        self.text = pygame.Surface((100, 150)).convert_alpha()
        self.text.fill((0, 0, 0, 0))
        text = pygame.font.Font(None, 20)
        textImg = text.render("New game", True, (0, 0, 255))
        self.text.blit(textImg, (10, 10))
        text = pygame.font.Font(None, 20)
        textImg = text.render("Highscores", True, (0, 0, 255))
        self.text.blit(textImg, (10, 40))
        text = pygame.font.Font(None, 20)
        textImg = text.render("Select Level", True, (0, 0, 255))
        self.text.blit(textImg, (10, 70))
        text = pygame.font.Font(None, 20)
        textImg = text.render("Credits", True, (0, 0, 255))
        self.text.blit(textImg, (10, 100))
        text = pygame.font.Font(None, 20)
        textImg = text.render("Exit", True, (0, 0, 255))
        self.text.blit(textImg, (10, 130))
        self.highlight = pygame.Surface((80, 20)).convert()
        self.highlight.fill((255, 0, 0))

    def run(self, screen, clock):
        result = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        result = (result - 1) % 5
                    if event.key == K_DOWN:
                        result = (result + 1) % 5
                    if event.key == K_RETURN:
                        return result
            screen.blit(self.background, (0, 0))
            screen.blit(self.highlight, (10, 30 * result))
            screen.blit(self.text, (0, 0))
            pygame.display.flip()
            clock.tick(const.FPS)
