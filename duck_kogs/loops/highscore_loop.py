"""
Module that includes the class HighscoreLoop
"""
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_LEFT, K_RIGHT
import pygame
from duck_kogs.loops import loop
from duck_kogs.loops import game_loop
from duck_kogs import const
import sys


class HighscoreLoop(loop.Loop):
    """
    The loop to play the game.
    """
    def __init__(self):
        super(HighscoreLoop, self).__init__()
        #TODO TEXTOS Y POSICIONES
        self.background = pygame.Surface((100, 150)).convert()
        self.background.fill((0, 255, 0))
        self.text = pygame.Surface((100, 150)).convert_alpha()
        self.render_text()

    def render_text(self):
        self.text.fill((0, 0, 0, 0))
        highscore_file = open(const.HIGHSCOREFILE,"r+")
        highscore_list = []
        for i in range(const.HIGHSCOREMAXVALUES):
            data = highscore_file.readline()
            data = data.split(",")
            highscore_list.append({"time":int(data[0]),"stage":int(data[1])})
        highscore_file.close()
        i = 0
        for score in highscore_list:
            text = pygame.font.Font(const.FONT, 20)
            to_print = ("Time:" + str(score["time"]) +
                    "    Stage:" + str(score["stage"]))
            text_img = text.render(to_print, True, (0, 0, 255))
            self.text.blit(text_img, (10, 10+20*i))
            i += 1

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
