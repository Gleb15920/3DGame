# -*- coding: utf-8 -*-
import pygame as pg
import pygame_gui
from settings import *


class CodeWindow:
    def __init__(self, game, code_controller):
        self.running = False
        self.game = game
        self.manager = pygame_gui.UIManager(screen, 'resources/theme.json')
        self.text_field = pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((width / 2 - 250, 300, 500, 70)),
                                                             manager=self.manager)
        self.submit_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 400, 500, 70)),
                                                       text='Try',
                                                       manager=self.manager)
        self.exit_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((470, 500, 500, 70)),
                                                     text='<-',
                                                     manager=self.manager)
        self.text_result = pygame_gui.elements.UILabel(relative_rect=pg.Rect((470, 200, 300, 70)),
                                                       manager=self.manager, text='')
        #
        # self.text_box = pygame_gui.elements.UILabel(relative_rect=pg.Rect(440, 100, 500, 70),
        #                                             manager=self.manager, text='enter the right code')
        if self.game.num_level == 0:
            self.start_bg = pg.image.load('resources/images/start_menu/subway_bg.jpg')
        elif self.game.num_level == 1:
            self.start_bg = pg.image.load('resources/images/start_menu/city_bg.jpg')
        else:
            self.start_bg = pg.image.load('resources/images/start_menu/start_background.jpg')

        self.start_bg = pg.transform.scale(self.start_bg, screen)
        self.clock = pg.time.Clock()
        self.game = game
        self.code_controller = code_controller
        self.text_field.on_hovered = lambda: self.text_result.set_text('')

    def run_start_menu(self):
        self.running = True
        self.text_field.focus()
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pg.event.get():
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if hasattr(event, 'ui_element') and event.ui_element == self.submit_btn:
                        code = self.text_field.get_text()
                        self.text_field.unfocus()
                        if self.code_controller.check_code(code):
                             self.running = False
                        else:
                            self.text_result.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
                            self.text_result.set_text("wrong code!!")
                    if (event.type == pygame_gui.UI_BUTTON_PRESSED and
                            hasattr(event, 'ui_element') and event.ui_element == self.exit_btn):
                        self.running = False

                if self.running:
                    self.manager.process_events(event)
            if self.running:
                self.manager.update(time_delta)
                self.game.screen.blit(self.start_bg, (0, 0))
                self.manager.draw_ui(self.game.screen)
                pg.display.update()
