import pygame as pg
from settings import music_volume, sound_volume


class Music:
    def __init__(self):
        pg.init()
        pg.mixer.music.set_volume(music_volume)
        pg.mixer.music.stop()
        self.metro_music = pg.mixer.Sound("resources/music/metro_music.wav")
        self.town_music1 = pg.mixer.Sound("resources/music/town_music1.wav")
        self.menu = pg.mixer.Sound("resources/music/town_music2.wav")
        self.boss_music = pg.mixer.Sound("resources/music/boss_music.wav")
        self.good_end_music = pg.mixer.Sound("resources/music/good_end_music.mp3")
        self.error_sound = pg.mixer.Sound("resources/music/error_sound.mp3")
        self.death_sound = pg.mixer.Sound("resources/music/death_sound.mp3")
        self.menu_music = pg.mixer.Sound("resources/music/menu_music.wav")

    def play(self, num_level):
        if num_level == 0:
            pg.mixer.music.stop()
            pg.mixer.music = self.metro_music
            pg.mixer.music.play(-1)
            pg.mixer.music.set_volume(music_volume)
        elif num_level == 1:
            pg.mixer.music.stop()
            pg.mixer.music = self.town_music1
            pg.mixer.music.play(-1)
            pg.mixer.music.set_volume(music_volume)
        elif num_level == 2:
            pg.mixer.music.stop()
            pg.mixer.music = self.boss_music
            pg.mixer.music.play(-1)
            pg.mixer.music.set_volume(music_volume)

    def good_end(self):
        pg.mixer.music.stop()
        pg.mixer.music = self.good_end_music
        pg.mixer.music.play()
        pg.mixer.music.set_volume(music_volume)

    def error(self):
        pg.mixer.music.stop()
        self.error_sound.play()

    def death(self):
        pg.mixer.music.stop()
        self.death_sound.play()

    def play_menu_music(self):
        pg.mixer.music.stop()
        pg.mixer.music = self.menu_music
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(music_volume)
