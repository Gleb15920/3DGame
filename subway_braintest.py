from settings import *


class Subway_Braintest():
    def __init__(self, game, sprites):
        self.game = game
        self.sprites = sprites

    def draw(self, screen):
        sprite_index = self.game.num_level - 1
        if sprite_index < 0 or sprite_index > len(self.sprites) - 1:
            return
        sprite = self.sprites[sprite_index]
        screen.blit(sprite, (self.game.layout_width -
                             self.game.player.x - width, 100))
        screen.blit(sprite, (self.game.layout_width -
                             self.game.player.x - width - 2000, 100))
        screen.blit(sprite, (self.game.layout_width -
                             self.game.player.x - width - 4000, 100))
        screen.blit(sprite, (self.game.layout_width -
                             self.game.player.x - width - 6000, 100))
