from setting import *


class Player(pygame.sprite.Sprite):

    def __init__(self,position,group):
        super().__init__(group)
        self.image = pygame.image.load(join("../images","player","down","0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = position)