from settings import *
import pygame as pg
from map import Map
from player import Player
import colors


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size)
        pg.event.set_grab(True)
        self.new_game()
        self.clock = pg.time.Clock()
        MOVE_DOWN_DELAY = 500
        MOVE_DOWN_EVENT = pg.USEREVENT + 1
        pg.time.set_timer(MOVE_DOWN_EVENT, MOVE_DOWN_DELAY)

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.layout_width = (len(self.map.map[0]) * tile_x)
        self.layout_height = (len(self.map.map) * tile_y)
        self.running = running

    def update(self):
        self.map.draw_map(self.screen)
        self.player.draw_player(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self.screen.fill(colors.black)
            self.player.control()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()