from screeninfo import get_monitors

size = width, height = get_monitors()[0].width, get_monitors()[0].height

speed = 80

arrow_amount = 4

to_left = False
to_right = False
running_gui_manager = True

vertical_velocity = 0
gravity = 2
hight_jump = 40

health = 1 * 1000 * 60  # time of life in minutes

music_volume = 1
sound_volume = 1
