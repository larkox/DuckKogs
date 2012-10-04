"""
Module that includes the Explosions_Group class
"""
from duck_kogs.sprites import dk_groups


class ExplosionsGroup(dk_groups.DKGroups):
    """
    Defines the explosion group behaviour.
    """
    instance = None
    is_init = False
    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

    def __init__(self, *sprites):
        if not self.is_init:
            super(ExplosionsGroup, self).__init__(*sprites)
            self.is_init = True
        else:
            self.add(*sprites)
