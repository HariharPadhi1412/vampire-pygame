from setting import *


class CollisionSprite(pygame.sprite.Sprite):

    def __init__(self,position,size,groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('blue')
        self.rect = self.image.get_frect(center = position)