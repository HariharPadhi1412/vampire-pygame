from setting import *
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Survivor")  
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites_grp = pygame.sprite.Group()

        # sprites
        self.player = Player((300,400),self.all_sprites_grp)

    def run(self):

        while self.running:

            # delta time
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.all_sprites_grp.update(self.display_surface)
            self.all_sprites_grp.draw(self.display_surface)        

            # draw
            pygame.display.update() 


        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()