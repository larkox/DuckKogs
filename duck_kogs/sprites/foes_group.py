"""
Module that include the FoesGroup class
"""
from duck_kogs.sprites import bomber_foe
from duck_kogs.sprites import fast_foe
from duck_kogs.sprites import angry_foe
from duck_kogs.sprites import master_foe
from duck_kogs.sprites import dk_groups


def bomber():
    """
    Switch element. Returns the constructor of the bomber foe.
    """
    return bomber_foe.BomberFoe

def fast():
    """
    Switch element. Returns the constructor of the fast foe.
    """
    return fast_foe.FastFoe

def angry():
    """
    Switch element. Returns the constructor of the angry foe.
    """
    return angry_foe.AngryFoe

def master():
    """
    Switch element. Returns the constructor of the master foe.
    """
    return master_foe.MasterFoe

class FoesGroup(dk_groups.DKGroups):
    """
    Group of Foes
    """
    Switch = {1: bomber(),
            2: fast(),
            3: angry(),
            4: master()}
    instance = None
    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance
    def __init__(self, map_file = None, game_map = None):
        if map_file:
            super(FoesGroup, self).__init__()
            for line in map_file:
                #file format: Type PosX PosY
                data = line.split(" ")
                new_sprite = FoesGroup.Switch[int(data[0])](
                        (int(data[1]), int(data[2])), game_map)
                self.add(new_sprite)
        else:
            pass

    def update(self, game_map):
        """
        Update the state of every foe regarding the game map.
        """
        for foe in self.sprites():
            foe.update(game_map)

    def get_on_pos(self, pos):
        for i in self.sprites():
            if i.pos == pos:
                return i
        return None
