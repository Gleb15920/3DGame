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

        self.walking = False

        self.not_walk()

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
        self.not_walk()
        pg.mixer.music.stop()
        pg.mixer.music = self.good_end_music
        pg.mixer.music.play()
        pg.mixer.music.set_volume(music_volume)

    def error(self):
        self.not_walk()
        pg.mixer.music.stop()
        self.error_sound.play()

    def death(self):
        self.not_walk()
        pg.mixer.music.stop()
        self.death_sound.play()

    def play_menu_music(self):
        self.not_walk()
        pg.mixer.music.stop()
        pg.mixer.music = self.menu_music
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(music_volume)

    def walk(self):
        if not self.walking:
            self.city_walking_sound.play()
            self.walking = True

    def not_walk(self):
        self.city_walking_sound.stop()
        self.walking = False

    def car(self):
        self.not_walk()
        self.car_sound.play()

    def hit(self):
        self.hit_sound.play()

    def teleport(self):
        self.not_walk()
        pg.mixer.music.stop()
        pg.mixer.music = self.teleport_sound
        pg.mixer.music.play()
        pg.mixer.music.set_volume(music_volume)
