"""
Main module of the game Duck Kogs
"""
import pygame
import game_loop
import menu_loop


def opt_new_game(screen, clock):
    """
    Switch option. Start the loop new game.
    """
    game_loop.GameLoop.LIVES = 3
    stages = ["mapa1.txt",
            "mapa2.txt",
            "mapa3.txt",
            "mapa4.txt"]
    loop_exit = False
    current_stage = 0
    while not loop_exit:
        exit_reason = game_loop.GameLoop(
                stages[current_stage], "texture1.png").run(screen, clock)
        if exit_reason == 0:
            game_loop.GameLoop.LIVES -= 1
        if exit_reason == 1:
            current_stage += 1
        if game_loop.GameLoop.LIVES < 0:
            loop_exit = True
        if current_stage > len(stages)-1:
            loop_exit = True
    return False


def opt_select_level(screen, clock):
    """
    Switch option. Start the loop select level.
    """
    return False


def opt_highscores(screen, clock):
    """
    Switch option. Start the loop highscores.
    """
    return False


def opt_credits(screen, clock):
    """
    Switch option. Start the loop credits.
    """
    return False


def opt_exit(screen, clock):
    """
    Switch option. Exits the game.
    """
    return True


Switch = {0: opt_new_game,
        1: opt_select_level,
        2: opt_highscores,
        3: opt_credits,
        4: opt_exit}


def main():
    """
    Main function of the game
    """
    #Setting up pygame
    user_exit = False
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
            (800,450))
    pygame.display.set_caption("Duck kogs")
    #TODO mejorar la forma de poner la resolucion
    #TODO Intro y Menu
    while not user_exit:
        user_exit = Switch[menu_loop.MenuLoop().run(screen, clock)](
                screen, clock)

if __name__ == "__main__":
    main()
