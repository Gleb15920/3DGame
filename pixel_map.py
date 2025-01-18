from random import choice
from PIL import Image
import numpy as np
import pygame as pg

import colors


class Pixel_map:
    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.create_void()
        self.set_settings()
        self.slide = 0

    def create_void(self):
        data_img = [[] for _ in range(int(self.level.tile_y / 2))]
        for i in range(len(data_img)):
            for j in range(int(self.level.tile_x / 2)):
                a = choice((colors.black, colors.white, colors.light_green, colors.dark_green))
                data_img[i].append(a)
                '''if choice((True, False)):
                    data_img[i].append([255, 255, 255])
                else:
                    data_img[i].append([0, 0, 0])'''
        data_img = np.array(data_img, dtype=np.uint8)
        img = Image.fromarray(data_img)
        self.img = img.resize((img.size[0] * 2, img.size[1] * 2))
        self.void_tile = pg.image.fromstring(self.img.tobytes(), self.img.size, self.img.mode)

    def set_settings(self):
        self.level.y += self.level.tile_y * (2/5)

    def draw_block(self, screen, cords):
        x, y = cords
        self.slide += 1
        if self.slide >= self.level.tile_y:
            self.slide = 0
        try:
            im = self.img.crop((0, self.img.size[1] - self.slide, self.img.size[0], self.img.size[1]))
            im = pg.image.fromstring(im.tobytes(), im.size, im.mode)
            screen.blit(im, (x, y))
        except: pass
        screen.blit(self.void_tile, (x, y + self.slide))