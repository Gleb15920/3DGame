from settings import *


class Subway_Braintest():
    def __init__(self, game, sprite):
        self.game = game
        self.sprite = sprite

    def draw(self, screen):
        screen.blit(self.sprite, (self.game.layout_width -
                                  self.game.player.x - width, 100))
        screen.blit(self.sprite, (self.game.layout_width -
                                  self.game.player.x - width - 2000, 100))
        screen.blit(self.sprite, (self.game.layout_width -
                                  self.game.player.x - width - 4000, 100))
        screen.blit(self.sprite, (self.game.layout_width -
                                  self.game.player.x - width - 6000, 100))