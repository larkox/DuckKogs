import pygame
from pygame.locals import *
import gameMap
import gameBucle
import bomberFoe
import sys
import const

def main():
    #Setting up pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((const.SQUAREDIM*5,const.SQUAREDIM*5))
    pygame.display.set_caption("Duck kogs")
    #TODO mejorar la forma de poner la resolucion
    #TODO Intro y Menu
    bucle = gameBucle.GameBucle("mapa1.txt","texture1.png")
    bucle.run(screen,clock)

if __name__ == "__main__":
    main()
