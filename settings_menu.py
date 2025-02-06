import pygame as pg
import pygame_gui
from pygame import SRCALPHA
import settings


class Settings:
    def __init__(self, game, size):
        self.running = False
        self.manager = pygame_gui.UIManager(size, 'resources/theme3.json')
        self.size = size
        self.surface = pg.Surface(size, SRCALPHA)
        self.clock = pg.time.Clock()
        self.game = game
        self.speed = settings.speed
        self.music_volume = settings.music_volume
        self.screen = game.screen
        self.volume_text = pygame_gui.elements.UILabel(relative_rect=pg.Rect((50, 50), (150, 30)),
                                                        text="Volume:",
                                                        manager=self.manager)

        self.volume_btn = pygame_gui.elements.UIHorizontalSlider(relative_rect=pg.Rect((200, 50), (200, 30)),
                                                                start_value=self.music_volume,
                                                                value_range=(0.0, 1.0),
                                                                manager=self.manager)

        self.speed_text = pygame_gui.elements.UILabel(relative_rect=pg.Rect((50, 100), (150, 30)),
                                                       text="Speed:",
                                                       manager=self.manager)

        self.speed_btn = pygame_gui.elements.UIHorizontalSlider(relative_rect=pg.Rect((200, 100), (200, 30)),
                                                               start_value=self.speed,
                                                               value_range=(40.0, 200.0),
                                                               manager=self.manager)
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect((self.size[0] // 2 - 100, self.size[1] - 100), (200, 50)),
            text='Back to Menu',
            manager=self.manager)

    def draw_menu(self):
        self.surface.fill((0, 0, 0, 0))
        color = (128, 128, 128, 150)
        pg.draw.rect(self.surface, color, [0, 0, self.size[0], self.size[1]])
        self.screen.blit(self.surface, (0, 0))

    def run_settings(self):
        self.running = True
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.game.running = False
                    self.running = False
                    break

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if hasattr(event, 'ui_element'):
                        if event.ui_element == self.back_button:
                            settings.music_volume = self.music_volume
                            settings.speed = self.speed
                            self.running = False

                elif event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if hasattr(event, 'ui_element'):
                        if event.ui_element == self.volume_btn:
                            self.music_volume = self.volume_btn.get_current_value()
                        elif event.ui_element == self.speed_btn:
                            self.speed = self.speed_btn.get_current_value()
                else:
                    self.manager.process_events(event)
            if self.running:
                self.manager.update(time_delta)
                self.draw_menu()
                self.manager.draw_ui(self.screen)
                pg.display.update()

