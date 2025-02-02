import pygame as pg
from settings import width, height
from settings import *
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

        self.pixboss = pg.image.load('resources/images/npc/pixman.png')
        h_boss = height
        w_boss = (320 * h_boss) / 419
        self.pixboss = pg.transform.scale(self.pixboss, (w_boss, h_boss))
        h_eye = height / 4
        w_eye = (380 * h_eye) / 200
        self.lastboss = pg.image.load('resources/images/npc/lastboss.png')
        self.lastboss = pg.transform.scale(self.lastboss, (w_eye, h_eye))

        self.vr = pg.image.load('resources/images/vr.png')
        w_vr = width
        h_vr = (w_vr * 339) / 757
        self.vr = pg.transform.scale(self.vr, (w_vr, h_vr))

        self.room = pg.image.load('resources/images/room.jpg')
        w_room = width
        h_room = (w_room * 720) / 1280
        self.room = pg.transform.scale(self.room, (w_room, h_room))

        self.stair = pg.image.load('resources/images/doors/stair.png')
        self.stair = pg.transform.scale(self.stair, (width / 2, self.game.levels[self.game.num_level].y +
                                                     self.game.levels[self.game.num_level].player_size[1]))

        self.bar = pg.image.load('resources/images/press.png')

        self.car = pg.image.load('resources/images/doors/car.png')
        self.car = pg.transform.scale(self.car, (self.tile_y * 2, self.tile_y))

        self.ept = pg.image.load('resources/images/doors/ept.png')
        h_ept = height / 5
        w_ept = (310 * h_ept) / 250
        self.ept = pg.transform.scale(self.ept, (w_ept, h_ept))

        self.doors = [(self.stair, 0), (self.car, self.game.levels[self.game.num_level].y +
                                        self.game.levels[self.game.num_level].player_size[1] -
                                        self.car.get_size()[1]), (self.ept, self.tile_y * 2 - h_ept)]

        self.arrow = pg.image.load('resources/images/braintests/arrow.png')
        self.arrow = pg.transform.scale(self.arrow, (width // 6, height // 3))

        self.radiation_effect = pg.image.load('resources/images/radiation_effect.png')
        self.radiation_effect = pg.transform.scale(self.radiation_effect, (width, height))

        self.walls = []
        for i in range(len([name for name in os.listdir('resources/images/walls')
                            if os.path.isfile(os.path.join('resources/images/walls', name))])):
            img = pg.image.load(f'resources/images/walls/{i}.jpg')
            img = pg.transform.scale(img, (self.tile_x, self.tile_y))
            self.walls.append(img)