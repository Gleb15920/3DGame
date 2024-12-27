from settings import *
from sprites import player_imgs_r, player_imgs_l, bar
import pygame as pg


class Player:
    def __init__(self, game):
        self.game = game
        self.size = player_size
        self.x = x
        self.y = y
        self.anim_shot = 0
        self.to_right = to_right
        self.to_left = to_left
        self.jump = jump
        self.player_imgs_r = player_imgs_r
        self.player_imgs_l = player_imgs_l
        self.animation = self.player_imgs_r
        self.cont = False # флаг для кнопки E

    def draw_player(self, screen):
        if self.x >= 0:
            screen.blit(self.animation[self.anim_shot - 1], (width / 2 - (self.size[0] / 2), self.y))
        elif self.x < 0:
            screen.blit(self.animation[self.anim_shot - 1], (width / 2 - (self.size[0] / 2) + self.x, self.y))
        if self.x >= self.game.layout_width - width - player_size[0] / 2:
            screen.blit(bar, (self.game.layout_width - self.x - width / 2, height / 2))
            self.cont = True
        else:
            self.cont = False

    def control(self):
        pg.time.delay(30)
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.game.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.to_left = True
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.to_right = True
                if event.key == pg.K_UP or event.key == pg.K_w or event.key == pg.K_SPACE:
                    if not self.jump[0]:
                        self.jump = [True, height_of_jump]
                if event.type == pg.K_e and self.cont:
                    pass # go to next level
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.to_left = False
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.to_right = False
        if self.to_left or self.to_right:
            if self.to_right:
                if self.game.layout_width - width - player_size[0] / 2 > self.x:
                    self.x += speed
                if self.anim_shot < len(self.animation):
                    self.anim_shot += 1
                else:
                    self.anim_shot = 1
                self.animation = self.player_imgs_r
            if self.to_left:
                if width / 2 - self.size[0] / 2 > -self.x:
                    self.x -= speed
                if self.anim_shot < len(self.animation):
                    self.anim_shot += 1
                else:
                    self.anim_shot = 1
                self.animation = self.player_imgs_l
        else:
            self.anim_shot = 1
        if self.jump[0]:
            if self.jump[1] > 0:
                if self.jump[1] > height_of_jump // 2:
                    self.y -= speed / 2
                else:
                    if self.y + speed <= tile_y * col_tile_y - self.size[1]:
                        self.y += speed / 2
                self.jump[1] -= 1
            else:
                self.jump = [False, 0]