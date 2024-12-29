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
    
    def draw_map(self , screen):
        x_player = self.game.player.x
        if x_player < 0:
            x_player = 0
        elif x_player > self.game.layout_width - width:
            x_player = self.game.layout_width - width
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'w':
                    screen.blit(self.walls[0], (j * self.tile_x - x_player, i * self.tile_y))
                elif self.map[i][j] == '_':
                    screen.blit(self.walls[1], (j * self.tile_x - x_player, i * self.tile_y))
                elif self.map[i][j] == 'x':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[2], (j * self.tile_x - x_player, i * self.tile_y))
                    else:
                        screen.blit(self.walls[3], (j * self.tile_x - x_player, i * self.tile_y))
                elif self.map[i][j] == 'z':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[4], (j * self.tile_x - x_player, i * self.tile_y))
                    else:
                        screen.blit(self.walls[5], (j * self.tile_x - x_player, i * self.tile_y))
                elif self.map[i][j] == 'c':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[6], (j * self.tile_x - x_player, i * self.tile_y))
                    else:
                        screen.blit(self.walls[7], (j * self.tile_x - x_player, i * self.tile_y))
                elif self.map[i][j] == 'p':
                    if i < len(self.map) // 2:
                        screen.blit(self.walls[8], (j * self.tile_x - x_player, i * self.tile_y))
                    else:
                        screen.blit(self.walls[9], (j * self.tile_x - x_player, i * self.tile_y))
                elif self.map[i][j] == '+':
                    if not self.animate:
                        screen.blit(self.doors[0], (self.game.layout_width -
                                                self.game.player.x - width / 2, self.doors[1]))