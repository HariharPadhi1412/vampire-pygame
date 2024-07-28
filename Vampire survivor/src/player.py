from setting import *

class Player(pygame.sprite.Sprite):

    def __init__(self,position,group):
        super().__init__(group)
        self.path = join('Vampire survivor\images','player','down','0.png')
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_frect(center = position)
        self.direction = pygame.math.Vector2()
        self.speed = 400

    def input(self):
        keys_pressed = pygame.key.get_pressed()
        self.direction.x = int(keys_pressed[pygame.K_RIGHT]) - int(keys_pressed[pygame.K_LEFT])
        self.direction.y = int(keys_pressed[pygame.K_DOWN]) - int(keys_pressed[pygame.K_UP])
        self.direction =  self.direction.normalize() if self.direction else self.direction

    def move(self,delta_time):
        self.rect.center += self.direction * self.speed * delta_time

    def update(self,delta_time):
        self.input()
        self.move(delta_time)