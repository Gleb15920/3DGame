from screeninfo import get_monitors

screen = width, height = get_monitors()[0].width, get_monitors()[0].height
mid_width = width // 2


speed = 30

arrow_amount = 4

to_left = False
to_right = False
running_gui_manager = True

vertical_velocity = 0
gravity = 2
hight_jump = 40