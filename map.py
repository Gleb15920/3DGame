from settings import *
from sprites import walls, npc_img
import pygame as pg


class Map:
    def __init__(self, game):
        self.game = game
        self.map = self.open_map('resources/map.txt')
        self.walls = walls
        self.npc = npc_img
        self.barriers = []
        
    def open_map(self, path):
        with open(path, 'r') as file:
            self.map = file.readlines()
        return [list(elem.replace('\n', '')) for elem in self.map]
    
    def draw_map(self , screen):
        x_player = self.game.player.x
        if x_player < 0:
            x_player = 0
        elif x_player > self.game.layout_width - width:
            x_player = self.game.layout_width - width
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'w':
                    screen.blit(self.walls[0], (j * tile_x - x_player, i * tile_y))
                elif self.map[i][j] == '_':
                    screen.blit(self.walls[1], (j * tile_x - x_player, i * tile_y))
                elif self.map[i][j] == 'x':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[2], (j * tile_x - x_player, i * tile_y))
                    else:
                        screen.blit(self.walls[3], (j * tile_x - x_player, i * tile_y))
                elif self.map[i][j] == 'z':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[4], (j * tile_x - x_player, i * tile_y))
                    else:
                        screen.blit(self.walls[5], (j * tile_x - x_player, i * tile_y))
                elif self.map[i][j] == 'c':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[6], (j * tile_x - x_player, i * tile_y))
                    else:
                        screen.blit(self.walls[7], (j * tile_x - x_player, i * tile_y))
                elif self.map[i][j] == '+':
                    if j > len(self.map[i]) // 2:
                        img = self.npc[0]
                        img = pg.transform.scale(img, (width / 2, tile_y * col_tile_y))
                        screen.blit(img, (self.game.layout_width - self.game.player.x - width / 2, 0))
                    else:
                        screen.blit(self.npc[1], (j * tile_x - x_player, i * tile_y))

