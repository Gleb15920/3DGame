from screeninfo import get_monitors

size = width, height = get_monitors()[0].width, get_monitors()[0].height

speed = width / 30
jump = [False, 0]
time_of_jump = 20

to_left = False
to_right = False
running = True