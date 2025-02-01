from settings import *


class Subway_Braintest:
    def __init__(self, game, sprites):
        self.game = game
        self.sprites = sprites
        self.len_sprites = len(sprites)


    def draw(self, screen):
        if self.game.num_level != 0:
            return

        # screen.blit(self.sprites[0], (self.game.layout_width -
        #                               self.game.player.x - width - 2000, 100))
        # screen.blit(self.sprites[1], (self.game.layout_width -
        #                               self.game.player.x - width - 5000, 100))
        # screen.blit(self.sprites[2], (self.game.layout_width -
        #                               self.game.player.x - width - 8000, 100))
        # screen.blit(self.sprites[3], (self.game.layout_width -
        #                               self.game.player.x - width - 11000, 100))
        distance = 2000
        for i in range(self.len_sprites):
            screen.blit(self.sprites[i], (self.game.layout_width -
                                          self.game.player.x - width - distance, 100))
            distance += 3000

