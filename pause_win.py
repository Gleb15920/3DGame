import pygame as pg
import pygame_gui


class Pause:
    def __init__(self, game, size, SCRALPHA=128):
        self.game = game
        self.size = size
        self.surface = pg.Surface(size, SCRALPHA)
        self.screen = game.screen
        self.clock = pg.time.Clock()
        self.pause = True
        self.manager = pygame_gui.UIManager(size, 'resources/theme.json')
        self.continue_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((size[0] // 2 - 200, size[1] // 2 - 200, 400, 70)),
                                                     text='Continue',
                                                     manager=self.manager)
        self.settings_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((size[0] // 2 - 200, size[1] // 2 - 100, 400, 70)),
                                                         text='Settings',
                                                         manager=self.manager)
        self.exit_btn = pygame_gui.elements.UIButton(relative_rect=pg.Rect((size[0] // 2 - 200, size[1] // 2, 400, 70)),
                                                         text='Back to start menu',
                                                         manager=self.manager)

    def esc_menu(self):
        self.surface.fill((0, 0, 0, 0))
        color = (128, 128, 128, 150)
        pg.draw.rect(self.surface, color, [0, 0, self.size[0], self.size[1]])
        self.screen.blit(self.surface, (0, 0))

    def pause_game(self):
        self.game.paused = True
        while self.game.paused:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pg.event.get():
                self.manager.process_events(event)
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if hasattr(event, 'ui_element') and event.ui_element == self.exit_btn:
                        self.game.running = False
                        self.game.paused = False
                        self.game.screensaver.run_start_menu()
                        break
                    if hasattr(event, 'ui_element') and event.ui_element == self.continue_btn:
                        self.game.paused = False
                        self.game.running = True
                    if hasattr(event, 'ui_element') and event.ui_element == self.settings_btn:
                        self.game.settings.run_settings()
                        self.game.running = False
                        self.game.pause = True

            if self.game.paused:
                self.manager.update(time_delta)
                self.esc_menu()
                self.screen.blit(self.surface, (0, 0))
                self.manager.draw_ui(self.screen)
                pg.display.flip()