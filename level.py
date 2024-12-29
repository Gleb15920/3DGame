from settings import width, height


class Level:
    def __init__(self, path, col_x, background):
        self.background = background
        self.map_path = path
        self.col_tile_x = col_x
        self.col_tile_y = 2
        self.tile_x = width / self.col_tile_x
        self.tile_y = height / self.col_tile_y
        p_height = (self.tile_y / 5) * 3
        p_width = (105 * p_height) / 137
        self.player_size = (p_width, p_height)
        self.x = 0
        self.y = self.col_tile_y * self.tile_y - self.player_size[1] - self.tile_y * (2/5)