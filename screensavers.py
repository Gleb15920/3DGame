import pygame as pg
import pygame_gui
from settings import *


class Screensaver:
    def __init__(self, game):
        self.screen = pg.display.set_mode(screen)
        self.running_gui_manager = running_gui_manager
        self.manager = pygame_gui.UIManager(screen, 'resources/theme.json')
        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 300, 500, 70)),
                                                      text='Start',
                                                      manager=self.manager)
        self.settings_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 400, 500, 70), ),
                                                         text='Settings',
                                                         manager=self.manager)
        self.exit_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 500, 500, 70), ),
                                                     text='Exit',
                                                     manager=self.manager)

        self.start_bg = pg.image.load('resources/images/start_menu/start_background.jpg')
        self.start_bg = pg.transform.scale(self.start_bg, screen)
        self.clock = pg.time.Clock()
        self.game = game
        self.screen = game.screen


    def run_start_menu(self):
        while self.running_gui_manager:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pg.event.get():
                if (event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or
                        (event.type == pygame_gui.UI_BUTTON_PRESSED and hasattr(event, 'ui_element') and event.ui_element == self.exit_btn)):
                    self.running_gui_manager = False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if hasattr(event, 'ui_element') and event.ui_element == self.start_btn:
                        self.running_gui_manager = False
                        self.game.run()
                    elif hasattr(event, 'ui_element') and event.ui_element == self.settings_btn:
                        pass
                if self.running_gui_manager:
                    self.manager.process_events(event)
            if self.running_gui_manager:
                self.manager.update(time_delta)
                self.screen.blit(self.start_bg, (0, 0))
                self.manager.draw_ui(self.screen)
                pg.display.update()

