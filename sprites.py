import pygame as pg
from settings import width, height
import os


class Sprites:
    def __init__(self, game):
        self.game = game
        self.tile_x = self.game.levels[self.game.num_level].tile_x
        self.tile_y = self.game.levels[self.game.num_level].tile_y
        self.player_imgs_r = []
        self.player_imgs_l = []
        for i in range(len([name for name in os.listdir('resources/images/sprite_player') # такая конструкция в range() считывает сколько файлов в папке
                            if os.path.isfile(os.path.join('resources/images/sprite_player', name))])):
            img = pg.image.load(f'resources/images/sprite_player/{i}.png')
            img = pg.transform.scale(img, self.game.levels[self.game.num_level].player_size)
            self.player_imgs_r.append(img)
            img = pg.transform.flip(img, True, False)
            self.player_imgs_l.append(img)

        self.npc_img = []
        for i in range(len([name for name in os.listdir('resources/images/npc')
                            if os.path.isfile(os.path.join('resources/images/npc', name))])):
            img = pg.image.load(f'resources/images/npc/{i}.png')
            self.npc_img.append(img)

        self.stair = pg.image.load('resources/images/doors/stair.png')
        self.stair = pg.transform.scale(self.stair, (width / 2, self.game.levels[self.game.num_level].y +
                                                     self.game.levels[self.game.num_level].player_size[1]))

        self.bar = pg.image.load('resources/images/press.png')

        self.car = pg.image.load('resources/images/doors/car.png')
        self.car = pg.transform.scale(self.car, (self.tile_y * 2, self.tile_y))

        self.doors = [(self.stair, 0), (self.car, self.game.levels[self.game.num_level].y +
                                        self.game.levels[self.game.num_level].player_size[1] -
                                        self.car.get_size()[1]), (0, 0)]

        self.walls = []
        for i in range(len([name for name in os.listdir('resources/images/walls')
                            if os.path.isfile(os.path.join('resources/images/walls', name))])):
            img = pg.image.load(f'resources/images/walls/{i}.jpg')
            img = pg.transform.scale(img, (self.tile_x, self.tile_y))
            self.walls.append(img)

    def set_doors(self):
        pass
