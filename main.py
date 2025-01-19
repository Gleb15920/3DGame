from pixel_map import Pixel_map
from settings import screen, running, width, running_gui_manager
import pygame as pg
from map import Map
from player import Player
from level import Level
import colors
from sprites import Sprites
from random import randrange
import pygame_gui


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(screen)
        self.num_level = 0 # !!!!!!!!!!!!!!!!
        pg.event.set_grab(True)
        self.new_game()
        self.clock = pg.time.Clock()
        MOVE_DOWN_DELAY = 500
        MOVE_DOWN_EVENT = pg.USEREVENT + 1
        pg.time.set_timer(MOVE_DOWN_EVENT, MOVE_DOWN_DELAY)

    def new_game(self):
        self.levels = [Level('resources/subway_map.txt', 2, 2, colors.dark_grey),
                       Level('resources/city_map.txt', 1, 2, colors.black),
                       Level('resources/forest_map.txt', 4, 2, colors.black),
                       Level('resources/void_map.txt', 4, 3, colors.white)]

        self.p_map = Pixel_map(self, self.levels[-1])
        self.sprites = Sprites(self)
        self.map = Map(self, self.levels[self.num_level].map_path)
        self.player = Player(self)
        self.layout_width = (len(self.map.map[0]) * self.levels[self.num_level].tile_x)
        self.layout_height = (len(self.map.map) * self.levels[self.num_level].tile_y)
        self.running_gui_manager = running_gui_manager
        self.running = running
        self.manager = pygame_gui.UIManager(screen, 'resources/theme.json')
        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 300, 500, 70)),
                                                    text='Start',
                                                    manager=self.manager)
        self.settings_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 400, 500, 70),),
                                                      text='Settings',
                                                      manager=self.manager)
        self.exit_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 500, 500, 70), ),
                                                         text='Exit',
                                                         manager=self.manager)

        self.start_bg = pg.image.load('resources/images/start_menu/start_background.jpg')
        self.start_bg = pg.transform.scale(self.start_bg, screen)
        self.clock = pg.time.Clock()

    def interferences(self):
        for _ in range(3):
            pos_r = randrange(0, width)
            pg.draw.line(self.screen, colors.black,
                         (pos_r, 0), (pos_r, width), width=2)

    def update(self):
        self.map.draw_map(self.screen)
        self.player.draw_player(self.screen)
        pg.display.update()

    def run_start_menu(self):
        while self.running_gui_manager:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pg.event.get():
                if (event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or
                        (event.type == pygame_gui.UI_BUTTON_PRESSED and hasattr(event, 'ui_element') and event.ui_element == self.exit_btn)):
                    self.running = False
                    self.running_gui_manager = False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if hasattr(event, 'ui_element') and event.ui_element == self.start_btn:
                        self.running = True
                        self.running_gui_manager = False
                        self.run()
                    elif hasattr(event, 'ui_element') and event.ui_element == self.settings_btn:
                        pass
                if self.running_gui_manager:
                    self.manager.process_events(event)
            if self.running_gui_manager:
                self.manager.update(time_delta)
                self.screen.blit(self.start_bg, (0, 0))
                self.manager.draw_ui(self.screen)
                pg.display.update()

    def run(self):
        while self.running:
            self.screen.fill(self.levels[self.num_level].background)
            self.player.control(self.screen)
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run_start_menu()