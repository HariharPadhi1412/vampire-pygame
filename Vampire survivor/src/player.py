from setting import *

class Player(pygame.sprite.Sprite):

    def __init__(self,position,group,collision_sprites):
        super().__init__(group)
        self.path = join('Vampire survivor\images','player','down','0.png')
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_frect(center = position)
        self.hitbox_rect = self.rect.inflate(-60,0)

        self.direction = pygame.math.Vector2()
        self.speed = 500
        self.collision_sprite = collision_sprites

    def input(self):
        keys_pressed = pygame.key.get_pressed()
        self.direction.x = int(keys_pressed[pygame.K_RIGHT]) - int(keys_pressed[pygame.K_LEFT])
        self.direction.y = int(keys_pressed[pygame.K_DOWN]) - int(keys_pressed[pygame.K_UP])
        self.direction =  self.direction.normalize() if self.direction else self.direction

    def move(self,delta_time):
        self.hitbox_rect.x += self.direction.x * self.speed * delta_time
        self.collision("Horizontal")
        self.hitbox_rect.y += self.direction.y * self.speed * delta_time
        self.collision("Vertical")
        self.rect.center = self.hitbox_rect.center

    def collision(self,direction):
        for sprite in self.collision_sprite:
            if sprite.rect.colliderect(self.rect):
                if direction == "Horizontal":
                    if self.rect.x > 0 : self.hitbox_rect.right = sprite.rect.left
                    if self.rect.x < 0 : self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.rect.y > 0 : self.hitbox_rect.top = sprite.rect.bottom
                    if self.rect.y < 0 : self.hitbox_rect.bottom = sprite.rect.top

    def update(self,delta_time):
        self.input()
        self.move(delta_time)