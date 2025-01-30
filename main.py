from pixel_map import Pixel_map
from settings import size, running, width
import pygame as pg
from map import Map
from player import Player
from level import Level
import colors
from sprites import Sprites
from random import randrange


class Game:
    def __init__(self):
        pg.init()
        self.running = False
        self.screen = pg.display.set_mode(size)
        self.num_level = 3 # !!!!!!!!!!!!!!!!
        pg.event.set_grab(True)
        self.new_game()
        self.clock = pg.time.Clock()
        MOVE_DOWN_DELAY = 500
        MOVE_DOWN_EVENT = pg.USEREVENT + 1
        pg.time.set_timer(MOVE_DOWN_EVENT, MOVE_DOWN_DELAY)

    def new_game(self):
        self.running = True
        self.levels = [Level('resources/subway_map.txt', 2, 2, colors.dark_grey),
                       Level('resources/city_map.txt', 1, 2, colors.black),
                       Level('resources/forest_map.txt', 4, 2, colors.black),
                       Level('resources/void_map.txt', 4, 3, colors.white)]
        self.sprites = Sprites(self)
        self.map = Map(self, self.levels[self.num_level].map_path)
        self.player = Player(self)
        self.layout_width = (len(self.map.map[0]) * self.levels[self.num_level].tile_x)
        self.layout_height = (len(self.map.map) * self.levels[self.num_level].tile_y)
        self.p_map = Pixel_map(self, self.levels[-1])

    def update(self):
        self.map.draw_map(self.screen)
        self.subway_braintest.draw(self.screen)
        self.player.draw_player(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self.screen.fill(self.levels[self.num_level].background)
            self.player.control(self.screen)
            self.update()

if __name__ == '__main__':
    game = Game()
    screensaver = Screensaver(game)
    screensaver.run_start_menu()