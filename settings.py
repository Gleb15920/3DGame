from screeninfo import get_monitors

screen = width, height = get_monitors()[0].width, get_monitors()[0].height

speed = 30

to_left = False
to_right = False
running_gui_manager = True
running = True

vertical_velocity = 0
gravity = 2