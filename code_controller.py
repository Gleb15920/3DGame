from settings import width, height, speed
import colors
import pygame as pg
from random import randint


class Code_controller:

    def __init__(self, player, game):
        self.player = player
        self.right_codes = ['4312', '321', 'ьщщт']
        self.game = game

    def is_checked(self, code):
        code = code.rstrip()
        level = self.player.game.num_level
        return code == self.right_codes[level]

    def check_code(self, code):
        code = code.rstrip()
        level = self.player.game.num_level
        levels_count = len(self.player.game.levels)
        screen = self.player.game.screen

        if not self.is_checked(code):
            return False

        if self.game.num_level < len(self.game.levels) - 1:
            if self.game.num_level == 1:
                self.brumbrum(screen)
                self.change_level(screen, 'base64')
            elif self.game.num_level == len(self.game.levels) - 1:
                self.change_level(screen, '!!! RUN !!!')
            else:
                self.change_level(screen, 'WHERE ARE YOU?')
            self.game.num_level += 1
            self.game.new_game()
        return True

    def change_level(self, screen, text):
        self.game.sound.teleport()
        self.game.health.do_pause()
        pg.draw.rect(screen, colors.black, (0, 0, width, height))
        for i in range(1500):
            pg.draw.rect(screen, colors.white, (randint(0, width),
                                                randint(0, height), 20, 20))
            pg.draw.rect(screen, colors.grey, (randint(0, width),
                                               randint(0, height), 20, 20))
        txt = pg.font.SysFont(None, width // 10)
        txt = txt.render(text, True, colors.red)
        screen.blit(txt, (width / 2 - txt.get_width() / 2, height / 2))
        pg.display.flip()
        pg.time.delay(800)

    def brumbrum(self, screen):
        self.game.sound.car()
        self.game.map.animate = True
        r = 0  # насколько машина далеко уехала
        for i in range(0, width // 2, int(speed)):
            pg.time.delay(30)
            screen.fill(colors.black)
            self.game.map.draw_map(screen)
            screen.blit(self.game.sprites.doors[1][0], (self.game.layout_width -
                                                        self.game.player.x - width / 2 + r,
                                                        self.game.sprites.doors[1][1]))
            pg.display.update()
            r += speed
        self.game.map.animate = False