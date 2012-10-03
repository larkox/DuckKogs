"""
Module that includes the Bombs_group class
"""
from duck_kogs.sprites import bomb
from duck_kogs.sprites import dk_groups


class BombsGroup(dk_groups.DKGroups):
    """
    Defines the bomb group behaviour.
    """
    instance = None
    is_init = False
    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

    def __init__(self, *sprites):
        if not self.is_init:
            super(BombsGroup, self).__init__(*sprites)
            self.is_init = True
        else:
            self.add(*sprites)
