from screeninfo import get_monitors

size = width, height = get_monitors()[0].width, get_monitors()[0].height

speed = width / 30

to_left = False
to_right = False
running = True

vertical_velocity = 0
gravity = 2