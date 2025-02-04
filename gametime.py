import pygame.draw
from pygame.time import get_ticks
import pygame as pg
from settings import width, height


class GameTimer:
    def __init__(self, duration, game):
        self.start_time = 0
        self.duration = duration
        self.active = False
        self.pause = False
        self.cur_time = 0
        self.game = game

    def activate(self):
        if not self.active:
            self.active = True
            self.start_time = get_ticks()
        elif self.pause:
            self.start_time += get_ticks() - self.cur_time
            self.pause = False

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def do_pause(self):
        self.pause = True
        print("ewfwefw")

    def check_time(self):
        self.cur_time = get_ticks()
        if self.cur_time - self.start_time <= self.duration:
            return 100 - (self.cur_time - self.start_time) / self.duration * 100
        self.deactivate()
        return 0

    def update(self, screen: pg.display):
        if self.active:
            self.draw_health_bar(screen, self.check_time())
            print(self.check_time())
            return True
        return False

    def draw_health_bar(self, screen, health):
        pygame.draw.rect(screen, "red", (20, height - 70, width - 40, 40))
        pygame.draw.rect(screen, "green", (20, height - 70, (width - 40) * health / 100, 40))
        pygame.draw.rect(screen, "white", (20, height - 70, width - 40, 40), width=1)


