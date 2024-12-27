import pygame as pg
from settings import *
import os


player_imgs_r = []
player_imgs_l = []
for i in range(len([name for name in os.listdir('resources/images/sprite_player')
                    if os.path.isfile(os.path.join('resources/images/sprite_player', name))])):
    img = pg.image.load(f'resources/images/sprite_player/{i}.png')
    img = pg.transform.scale(img, player_size)
    player_imgs_r.append(img)
    img = pg.transform.flip(img, True, False)
    player_imgs_l.append(img)


npc_img = []
for i in range(len([name for name in os.listdir('resources/images/npc')
                    if os.path.isfile(os.path.join('resources/images/npc', name))])):
    img = pg.image.load(f'resources/images/npc/{i}.png')
    npc_img.append(img)

bar = pg.image.load(f'resources/images/press.png')

walls = []
for i in range(len([name for name in os.listdir('resources/images/walls')
                    if os.path.isfile(os.path.join('resources/images/walls', name))])):
    img = pg.image.load(f'resources/images/walls/{i}.jpg')
    img = pg.transform.scale(img, (tile_x, tile_y))
    walls.append(img)