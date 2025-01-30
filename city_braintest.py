from settings import *

class City_Braintest():
    def __init__(self, game, sprite):
        self.game = game
        self.sprite = sprite

    def draw(self, screen):
        if self.game.num_level == 1:
             screen.blit(self.sprite, (self.game.layout_width -
                                       self.game.player.x - width - 900, 100))