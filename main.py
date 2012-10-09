"""
Main module of the game Duck Kogs
"""
import pygame
import dircache
from duck_kogs import loops
from duck_kogs import const


STAGESLIST = []

def opt_new_game(screen, clock):
    """
    Switch option. Start the loop new game.
    """
    loops.game_loop.GameLoop.LIVES = const.NEWGAMELIVES
    loop_exit = False
    current_stage = 0
    total_time = 0
    while not loop_exit:
        (exit_reason, time) = loops.game_loop.GameLoop(
                main.STAGESLIST[current_stage]).run(screen, clock)
        if exit_reason == const.EXITDIED:
            loops.game_loop.GameLoop.LIVES -= 1
        if exit_reason == const.EXITWON:
            current_stage += 1
            total_time += time
        if loops.game_loop.GameLoop.LIVES < 0:
            loop_exit = True
        if current_stage > len(main.STAGESLIST) - 1:
            loop_exit = True
    store_highscore(total_time, current_stage - 1)
    return False


def store_highscore(time, stage):
    highscore_file = open(const.HIGHSCOREFILE,"r+")
    highscore_list = []
    for i in range(const.HIGHSCOREMAXVALUES):
        data = highscore_file.readline()
        data = data.split(",")
        highscore_list.append({"time":int(data[0]),"stage":int(data[1])})
    highscore_file.close()
    i = 0
    for elem in highscore_list:
        if elem["stage"] < stage:
            highscore_list = (highscore_list[:i] +
                    [{"time":int(time),"stage":stage}] +
                    highscore_list[i:])
            break
        elif elem["stage"] == stage:
            if elem["time"] > time:
                highscore_list = (highscore_list[:i] +
                        [{"time":int(time),"stage":stage}] +
                        highscore_list[i:])
                break
        i += 1
    highscore_file = open(const.HIGHSCOREFILE,"w")
    for i in range(const.HIGHSCOREMAXVALUES):
        elem = highscore_list[i]
        highscore_file.write(str(elem["time"]) + ", " + str(elem["stage"]) + "\n")

def opt_select_level(screen, clock):
    """
    Switch option. Start the loop select level.
    """
    loops.SelectLevelLoop(main.STAGESLIST).run(screen,clock)
    return False


def opt_highscores(screen, clock):
    """
    Switch option. Start the loop highscores.
    """
    loops.HighscoreLoop().run(screen,clock)
    return False


def opt_credits(screen, clock):
    """
    Switch option. Start the loop credits.
    """
    loops.CreditsLoop().run(screen,clock)
    return False


def opt_exit(screen, clock):
    """
    Switch option. Exits the game.
    """
    return True


SWITCH = {0: opt_new_game,
        1: opt_highscores,
        2: opt_select_level,
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
            (const.SCREENWIDTH,const.SCREENHEIGHT))
    pygame.display.set_caption(const.CAPTION)
    main.STAGESLIST = dircache.listdir(const.STAGESDIR)
    main.STAGESLIST = map(lambda x: const.STAGESDIR+x, main.STAGESLIST)
    #TODO Intro
    while not user_exit:
        user_exit = SWITCH[loops.menu_loop.MenuLoop().run(screen, clock)](
                screen, clock)

if __name__ == "__main__":
    main()
