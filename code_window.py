import pygame as pg
import pygame_gui
from settings import size


class CodeWindow:
    def __init__(self, game):
        self.screen = pg.display.set_mode(size)
        self.running = False
        self.manager = pygame_gui.UIManager(size, 'resources/theme.json')
        self.text_field = pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((470, 300, 500, 70)),
                                                      manager=self.manager)
        self.submit_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 400, 500, 70)),
                                                       text='Try',
                                                       manager=self.manager)
        self.start_bg = pg.image.load('resources/images/start_menu/start_background.jpg')
        self.start_bg = pg.transform.scale(self.start_bg, size)
        self.clock = pg.time.Clock()
        self.game = game
        self.screen = game.screen


    def run_start_menu(self):
        self.running = True
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pg.event.get():
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if hasattr(event, 'ui_element') and event.ui_element == self.submit_btn:
                        self.running = False
                if self.running:
                    self.manager.process_events(event)
            if self.running:
                self.manager.update(time_delta)
                self.screen.blit(self.start_bg, (0, 0))
                self.manager.draw_ui(self.screen)
                pg.display.update()

