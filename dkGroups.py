import pygame


class DKGroups(pygame.sprite.Group):
    def __init__(self):
        super(DKGroups,self).__init__()
    def draw(self,surface,gameMapRect):
        print gameMapRect.topleft
        for sprite in self.sprites():
            newRect = pygame.Rect(
                gameMapRect.left + sprite.rect.left,
                gameMapRect.top + sprite.rect.top,
                sprite.rect.width, sprite.rect.height)
            surface.blit(sprite.image,newRect)
