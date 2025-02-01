from settings import *


class Forest_Braintest:
    def __init__(self, game, sprite):
        self.game = game
        self.sprite = sprite

    def draw(self, screen):
        if self.game.num_level != 2:
            return
        screen.blit(self.sprite, (self.game.layout_width -
                                    self.game.player.x - 6000, 30))