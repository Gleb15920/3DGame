from random import choice
from PIL import Image
import numpy as np
from settings import width, height
import pygame as pg
import colors


class Pixel_map:
    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.void_tile = self.create_void((colors.black, colors.white, colors.light_green, colors.dark_green))
        img = Image.fromarray(np.array([[[0, 0, 0]]], dtype=np.uint8))
        self.dark_side_block = img.resize((int(width), int(height)))
        self.void_block = self.create_void((colors.white, colors.black))
        self.set_settings()
        self.slide = 0

        self.eye_boss = self.game.sprites.lastboss
        self.monolog_bad_ending = ['Вот мы и встретились', 'Трудно наверное тебе пришлось здесь',
                                   'я твоё глубокое подсознание',
                                   'к сожалению ты не успел вовремя убежать...',
                                   'и высшие силы отформатировали этот мир', 'теперь мы будем вместе в этой пустоте',
                                   '...']
        self.monolog_good_ending = ['Аааах', 'цифровая пустота', 'а я тебя недооценил',
                                   '0JrRgtC+INC/0YDQvtGH0LjRgtCw0Lsg0YLQvtGCINC70L7RhSE=', 'Умоляю']
        self.frase = 0

        self.all_sprites = pg.sprite.Group()
        self.sprite = pg.sprite.Sprite(self.all_sprites)
        self.sprite.image = self.game.sprites.pixboss
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = -width/2
        self.sprite.rect.y = 0

        self.im = self.dark_side_block.crop((0, 0, 1, 1))
        self.im = pg.image.fromstring(self.im.tobytes(), self.im.size, self.im.mode)

    def good_end(self, screen):
        self.game.sound.good_end()
        vr_image = self.game.sprites.vr
        screen.blit(vr_image, (0, height / 2 - vr_image.get_height() / 2))
        pg.display.flip()
        pg.time.delay(2000)
        done = False
        clock = pg.time.Clock()
        steps = 30
        frame_count = 0
        self.image = vr_image
        original_width, original_height = self.image.get_size()
        new_width, new_height = original_width // 2, original_height // 2
        while not done:
            screen.blit(self.game.sprites.room, (0, 0))
            if frame_count <= steps:
                current_width = int(original_width - (original_width - new_width) * frame_count / steps)
                current_height = int(original_height - (original_height - new_height) * frame_count / steps)
                resized_image = pg.transform.scale(self.image, (current_width, current_height))
                image_rect = resized_image.get_rect(center=(width // 2, height // 2))
                screen.blit(resized_image, image_rect)
                frame_count += 1
            else:
                resized_image = pg.transform.scale(self.image, (new_width, new_height))
                image_rect = resized_image.get_rect(center=(width // 2, height // 2))
                self.image = resized_image
                screen.blit(resized_image, image_rect)
                done = True
            pg.display.flip()
            clock.tick(60)
        done = False
        steps = 30
        frame_count = 0
        initial_y = height // 2
        final_y = self.image.get_height() / 4
        while not done:
            screen.blit(self.game.sprites.room, (0, 0))
            if frame_count <= steps:
                current_y = int(initial_y - (initial_y - final_y) * frame_count / steps)
                image_rect = self.image.get_rect(center=(width // 2, current_y))
                screen.blit(self.image, image_rect)
                frame_count += 1
            else:
                pg.time.delay(2000)
                any_key = True
                while any_key:
                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            any_key = False
                    image_rect = self.image.get_rect(center=(width // 2, final_y))
                    screen.blit(self.image, image_rect)
                    done = True
                    txt = pg.font.SysFont(None, 48)
                    txt = txt.render('Хорошая концовка\nНажмите любую кнопку, чтобы продолжить', True, colors.white)
                    screen.blit(txt, (width / 2 - txt.get_width() / 2, height / 2))
                    pg.display.flip()
            pg.display.flip()
        self.game.screensaver.running_gui_manager = True
        self.game.screensaver.run_start_menu()

    def bad_end(self, screen):
        bdos = pg.image.load('resources/images/BDoS.jpg')
        w_bdos = width
        h_bdos = (w_bdos * 768) / 1366
        bdos = pg.transform.scale(bdos, (w_bdos, h_bdos))
        screen.blit(bdos, (0, 0))
        self.game.sound.error()
        pg.display.flip()
        pg.time.delay(3000)
        self.game.screensaver.running_gui_manager = True
        self.game.screensaver.run_start_menu()

    def boss(self, screen):
        if self.game.num_level == len(self.game.levels) - 1:
            if self.im.get_width() >= width:
                self.game.running = False
                self.game.sound.not_walk()
                monolog = self.monolog_good_ending if self.game.player.is_go_to_end else self.monolog_bad_ending
                while True:
                    screen.fill(colors.black)
                    self.game.player.y = self.game.player.level.y
                    screen.blit(self.im, (0, 0))
                    for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if self.frase != len(monolog) - 1:
                                self.frase += 1
                            else:
                                if self.game.player.is_go_to_end:
                                    self.good_end(screen)
                                else:
                                    self.bad_end(screen)
                                return
                    screen.blit(self.eye_boss, (width / 2 - self.eye_boss.get_width() / 2, 0))
                    txt = pg.font.SysFont(None, 48)
                    txt = txt.render(monolog[self.frase], True, colors.pink)
                    screen.blit(txt, (width / 2 - txt.get_width() / 2, height / 2))
                    self.game.player.draw_player(screen)
                    pg.display.flip()
            else:
                self.sprite.rect.x += self.game.settings.speed * 0.15
                self.all_sprites.draw(screen)
                try:
                    self.im = self.dark_side_block.crop((0, 0, int(self.sprite.rect.x), height))
                    self.im = pg.image.fromstring(self.im.tobytes(), self.im.size, self.im.mode)
                    screen.blit(self.im, (0, 0))
                except:
                    self.im = self.dark_side_block.crop((0, 0, 1, 1))
                    self.im = pg.image.fromstring(self.im.tobytes(), self.im.size, self.im.mode)

    def create_void(self, color):
        data_img = [[] for _ in range(int(self.level.tile_y / 2))]
        for i in range(len(data_img)):
            for j in range(int(self.level.tile_x / 2)):
                a = choice(color)
                data_img[i].append(a)
        data_img = np.array(data_img, dtype=np.uint8)
        img = Image.fromarray(data_img)
        self.img = img.resize((img.size[0] * 2, img.size[1] * 2))
        return pg.image.fromstring(self.img.tobytes(), self.img.size, self.img.mode)

    def set_settings(self):
        self.level.y += self.level.tile_y * (2/5)

    def draw_block(self, screen, cords):
        x, y = cords
        self.slide += 1
        if self.slide >= self.level.tile_y:
            self.slide = 0
        try:
            im = self.img.crop((0, self.img.size[1] - self.slide, self.img.size[0], self.img.size[1]))
            im = pg.image.fromstring(im.tobytes(), im.size, im.mode)
            screen.blit(im, (x, y))
        except: pass
        screen.blit(self.void_block, (x, y + self.slide))

    def death(self, screen):
        self.game.running = False
        death = True
        self.game.sound.death()
        while death:
            screen.fill("black")
            txt = pg.font.SysFont(None, 48)
            txt = txt.render("Game Over!", True, colors.white)
            screen.blit(txt, (width / 2 - txt.get_width() / 2, height / 2))
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    death = False
                    self.game.screensaver.running_gui_manager = True
                    self.game.screensaver.run_start_menu()
            pg.display.flip()

