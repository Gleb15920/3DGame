from random import choice
from PIL import Image
import numpy as np
import pygame as pg


class Pixel_map:
    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.creat_tile()
        self.set_settings()

    def creat_tile(self):
        data_img = [[] for _ in range(int(self.level.tile_y / 2))]
        for i in range(len(data_img)):
            for j in range(int(self.level.tile_x / 2)):
                if choice((True, False)):
                    data_img[i].append([255, 255, 255])
                else:
                    data_img[i].append([0, 0, 0])
        data_img = np.array(data_img, dtype=np.uint8)
        img = Image.fromarray(data_img)
        img = img.resize((img.size[0] * 2, img.size[1] * 2))
        self.void_tile = pg.image.fromstring(img.tobytes(), img.size, img.mode)

    def set_settings(self):
        self.level.y += self.level.tile_y * (2/5)