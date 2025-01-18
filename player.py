import colors
from settings import *
import pygame as pg
from random import randint


class Player:
    def __init__(self, game):
        self.game = game
        self.level = self.game.levels[self.game.num_level]
        self.size = self.level.player_size
        self.x = self.level.x
        self.y = self.level.y
        self.anim_shot = 0
        self.to_right = to_right
        self.to_left = to_left
        self.bar = self.game.sprites.bar
        self.player_imgs_r = self.game.sprites.player_imgs_r
        self.player_imgs_l = self.game.sprites.player_imgs_l
        self.animation = self.player_imgs_r
        self.cont = False # флаг для кнопки E
        self.vertical_velocity = vertical_velocity
        self.jump = False
        self.ceil = 0
        self.ground = 0
        self.wall = 0

    def draw_player(self, screen):
        if self.x >= 0:
            screen.blit(self.animation[self.anim_shot - 1], (width / 2 - (self.size[0] / 2), self.y))
        elif self.x < 0:
            screen.blit(self.animation[self.anim_shot - 1], (width / 2 - (self.size[0] / 2) + self.x, self.y))
        if self.x >= self.game.layout_width - width - self.size[0] / 2:
            if self.game.num_level != 3:
                screen.blit(self.bar, (self.game.layout_width - self.x - width / 2, height / 2))
            self.cont = True
        else:
            self.cont = False

    def change_level(self, screen, text):
        pg.draw.rect(screen, colors.black, (0, 0, width, height))
        for i in range(1500):
            pg.draw.rect(screen, colors.white, (randint(0, width),
                                                randint(0, height), 20, 20))
            pg.draw.rect(screen, colors.grey, (randint(0, width),
                                               randint(0, height), 20, 20))
        txt = pg.font.SysFont(None, width // 10)
        txt = txt.render(text, True, colors.red)
        screen.blit(txt, (width / 5, height / 2))
        pg.display.flip()
        pg.time.delay(800)

    def brumbrum(self, screen):
        self.game.map.animate = True
        r = 0 # насколько машина далеко уехала
        for i in range(0, width // 2, int(speed)):
            pg.time.delay(30)
            screen.fill(colors.black)
            self.game.map.draw_map(screen)
            screen.blit(self.game.sprites.doors[1][0], (self.game.layout_width -
                                        self.game.player.x - width / 2 + r, self.game.sprites.doors[1][1]))
            pg.display.update()
            r += speed
        self.game.map.animate = False

    def control(self, screen):
        pg.time.delay(30)
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.game.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.to_left = True
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.to_right = True
                if event.key == pg.K_UP or event.key == pg.K_w or event.key == pg.K_SPACE:
                    if not self.jump:
                        self.vertical_velocity = -40
                        self.jump = True
                if event.key == pg.K_e and self.cont:
                    if self.game.num_level < len(self.game.levels) - 1:
                        if self.game.num_level == 1:
                            self.brumbrum(screen)
                            self.change_level(screen, 'WHERE ARE YOU?')
                        elif self.game.num_level == 2:
                            self.change_level(screen, '! ! ! ! !  RUN  ! ! ! ! !')
                        else:
                            self.change_level(screen, 'WHERE ARE YOU?')
                        self.game.num_level += 1
                        self.game.new_game()
                    else:
                        pass # конец игры
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.to_left = False
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.to_right = False
        if self.to_left or self.to_right:
            if self.to_right:
                if self.game.layout_width - width - self.size[0] / 2 > self.x:
                    """barrier = [elem[0] for elem in self.game.map.barriers]
                    val = (self.y // self.level.tile_y + 1) * self.level.tile_y
                    if val in barrier:
                        list = [elem[0] for elem in self.game.map.barriers if elem[1] == val]
                        self.wall = min(list, key=lambda x: abs(x - self.x)) - self.level.tile_y - self.size[0]
                    print(self.x, self.wall, barrier)
                    if self.wall >= self.x:"""
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

        if self.y < self.ceil:
            self.vertical_velocity = 5
        self.vertical_velocity += gravity
        self.y += self.vertical_velocity
        self.ground = self.level.y
        self.ceil = 0
        barrier = [elem[0] for elem in self.game.map.barriers]
        val = (self.x // self.level.tile_x + 1) * self.level.tile_x
        if val in barrier:
            list = [elem[1] for elem in self.game.map.barriers if elem[0] == val]
            self.ground = min(list) + self.level.tile_y * (2 / 5)
            if self.ground < 0:
                list.remove(self.ground - self.level.tile_y * (2 / 5))
                self.ground = min(list) + self.level.tile_y * (2 / 5)
            if len(list) == 1:
                self.ceil = self.ground + self.level.tile_y + self.level.tile_y * (2 / 5)
            else:
                list.remove(self.ground - self.level.tile_y * (2 / 5))
                self.ceil = abs(max(list))
            if self.ceil > self.y:
                self.ceil = 0
        if self.y > self.ceil and not (self.ceil < self.ground < self.level.y):
            self.ground = self.level.y
        if self.y >= self.ground:
            self.y = self.ground
            self.vertical_velocity = 0
            self.jump = False