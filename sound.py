import random

import pygame as pg
from settings import music_volume, sound_volume


class Sound:
    def __init__(self):
        pg.init()
        pg.mixer.music.set_volume(music_volume)
        pg.mixer.music.stop()
        self.metro_music = pg.mixer.Sound("resources/music/metro_music.wav")
        self.town_music = pg.mixer.Sound("resources/music/town_music1.wav")
        self.boss_music = pg.mixer.Sound("resources/music/boss_music.wav")
        self.good_end_music = pg.mixer.Sound("resources/music/good_end_music.mp3")
        self.death_sound = pg.mixer.Sound("resources/music/death_sound.mp3")
        self.menu_music = pg.mixer.Sound("resources/music/menu_music.wav")

        self.error_sound = pg.mixer.Sound("resources/sound/error_sound.mp3")
        self.metro_walking_sound = pg.mixer.Sound("resources/sound/metro_walking_sound.mp3")
        self.city_walking_sound = pg.mixer.Sound("resources/sound/city_walking_sound.mp3")
        self.car_sound = pg.mixer.Sound("resources/sound/car_sound.mp3")
        self.hit_sound = pg.mixer.Sound("resources/sound/hit_sound.mp3")
        self.teleport_sound = pg.mixer.Sound("resources/sound/teleport_sound.mp3")
        self.jump_sound = pg.mixer.Sound("resources/sound/jump_sound.mp3")
        self.geiger_sound = pg.mixer.Sound("resources/sound/geiger_click.mp3")

        self.walking = False
        self.health = 100
        self.not_walk()
        self.geiger_sound.stop()

    def update(self, num_level):
        if num_level == 0:
            pg.mixer.music.stop()
            pg.mixer.music = self.metro_music
            pg.mixer.music.play(-1)
            pg.mixer.music.set_volume(music_volume)
        elif num_level == 1:
            pg.mixer.music.stop()
            pg.mixer.music = self.town_music
            pg.mixer.music.play(-1)
            pg.mixer.music.set_volume(music_volume)
        elif num_level == 2:
            pg.mixer.music.stop()
            pg.mixer.music = self.boss_music
            pg.mixer.music.play(-1)
            pg.mixer.music.set_volume(music_volume)

    def good_end(self):
        self.geiger_sound.stop()
        self.not_walk()
        pg.mixer.music.stop()
        pg.mixer.music = self.good_end_music
        pg.mixer.music.play()
        pg.mixer.music.set_volume(music_volume)

    def error(self):
        self.geiger_sound.stop()
        self.not_walk()
        pg.mixer.music.stop()
        self.error_sound.play()

    def death(self):
        self.geiger_sound.stop()
        self.not_walk()
        pg.mixer.music.stop()
        self.death_sound.play()

    def play_menu_music(self):
        self.geiger_sound.stop()
        self.not_walk()
        pg.mixer.music.stop()
        pg.mixer.music = self.menu_music
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(music_volume)

    def walk(self):
        if not self.walking:
            self.city_walking_sound.play()
            self.city_walking_sound.set_volume(sound_volume)
            self.walking = True

    def not_walk(self):
        self.city_walking_sound.stop()
        self.walking = False

    def car(self):
        self.not_walk()
        self.car_sound.play()
        self.car_sound.set_volume(sound_volume)

    def hit(self):
        self.hit_sound.play()
        self.hit_sound.set_volume(sound_volume)

    def teleport(self):
        self.not_walk()
        pg.mixer.music.stop()
        self.teleport_sound.play()
        self.teleport_sound.set_volume(sound_volume)

    def jump(self):
        self.jump_sound.play()
        self.jump_sound.set_volume(sound_volume)

    def geiger(self, health):
        health = round(health)
        if health <= 50:
            if health % (random.randint(health // 10 + 1, 11)) == 0 and self.health != health:
                self.geiger_sound.play()
                self.health = health
