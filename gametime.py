from pygame.time import get_ticks
import pygame as pg


class GameTimer:
    def __init__(self, duration):
        self.start_time = 0
        self.duration = duration
        self.active = False
        self.pause = False
        self.cur_time = 0

    def activate(self):
        print("fwefwef")
        if not self.active and not self.pause:
            print("wpoi")
            self.active = True
            self.start_time = get_ticks()
        elif self.pause:
            self.start_time += get_ticks() - self.cur_time
            self.active = True
            self.pause = False
            print("dqdq")

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def do_pause(self):
        self.active = False
        self.pause = True

    def check_time(self):
        if self.active:
            self.cur_time = get_ticks()
            if self.cur_time - self.start_time <= self.duration:
                return round(100 - (self.cur_time - self.start_time) / self.duration * 100)

    def update(self, screen: pg.display):
        if self.active:
            text = pg.font.Font(None, 100).render(str(self.check_time()), False, "white")
            screen.blit(text, (100, 100))
            # print(self.active, self.check_time())
