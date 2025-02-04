from settings import width


class Map:
    def __init__(self, game, path):
        self.game = game
        self.map = self.open_map(path)
        self.walls = self.game.sprites.walls
        self.doors = self.game.sprites.doors[self.game.num_level]
        self.barriers = []
        self.tile_x = self.game.levels[self.game.num_level].tile_x
        self.tile_y = self.game.levels[self.game.num_level].tile_y
        self.animate = False

    def open_map(self, path):
        with open(path, 'r') as file:
            self.map = file.readlines()
        return [list(elem.replace('\n', '')) for elem in self.map]

    def draw_map(self, screen):
        self.barriers = []
        x_player = self.game.player.x
        if x_player < 0:
            x_player = 0
        elif x_player > self.game.layout_width - width:
            x_player = self.game.layout_width - width
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                cords = (j * self.tile_x - x_player, i * self.tile_y)
                if self.map[i][j] == 'w':
                    screen.blit(self.walls[0], cords)
                elif self.map[i][j] == '_':
                    screen.blit(self.walls[1], cords)
                elif self.map[i][j] == 'x':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[2], cords)
                    else:
                        screen.blit(self.walls[3], cords)
                elif self.map[i][j] == 'z':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[4], cords)
                    else:
                        screen.blit(self.walls[5], cords)
                elif self.map[i][j] == 'c':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[6], cords)
                    else:
                        screen.blit(self.walls[7], cords)
                elif self.map[i][j] == 'p':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[8], cords)
                    else:
                        screen.blit(self.walls[9], cords)
                elif self.map[i][j] == ',':
                    screen.blit(self.game.p_map.void_tile, cords)
                elif self.map[i][j] == '#':
                    self.game.p_map.draw_block(screen, cords)
                    self.barriers.append(((j + 1) * self.tile_x - width / 2, (i - 1) * self.tile_y))
                if not self.animate:
                    screen.blit(self.doors[0], (self.game.layout_width -
                                                self.game.player.x - width / 2, self.doors[1]))
