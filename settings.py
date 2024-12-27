from screeninfo import get_monitors

size = width, height = get_monitors()[0].width, get_monitors()[0].height
col_tile_y = 3
col_tile_x = col_tile_y * 2
tile_x = width / col_tile_x
tile_y = height / col_tile_y

p_height = (tile_y / 5) * 3
p_width = (105 * p_height) / 137
player_size = (p_width, p_height)
x = 0
y = col_tile_y * tile_y - player_size[1] - (tile_y / 5) * 2
speed = width / 30
jump = [False, 0]
height_of_jump = 20

to_left = False
to_right = False
running = True