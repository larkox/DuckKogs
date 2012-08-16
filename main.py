import pygame
from pygame.locals import *
import gameMap
import gameLoop
import menuLoop
import bomberFoe
import sys
import const


def newGame(screen, clock):
    gameLoop.GameLoop("mapa1.txt", "texture1.png").run(screen, clock)
    return False


def selectLevel(screen, clock):
    return False


def highscores(screen, clock):
    return False


def credits(screen, clock):
    return False


def exit(screen, clock):
    return True


Switch = {0: newGame,
        1: selectLevel,
        2: highscores,
        3: credits,
        4: exit}


def main():
    #Setting up pygame
    exit = False
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
            (800,450))
    pygame.display.set_caption("Duck kogs")
    #TODO mejorar la forma de poner la resolucion
    #TODO Intro y Menu
    while not exit:
        exit = Switch[menuLoop.MenuLoop().run(screen, clock)](screen, clock)

if __name__ == "__main__":
    main()
