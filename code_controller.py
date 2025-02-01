
class Code_controller:

    def __init__(self, player):
        self.player = player
        self.right_codes = ['4312', '1', 'ьщщт']

    def is_checked(self, code):
        code = code.rstrip()
        level = self.player.game.num_level
        return code == self.right_codes[level]

    def check_code(self, code):
        code = code.rstrip()
        level = self.player.game.num_level
        levels_count = len(self.player.game.levels)
        screen = self.player.game.screen

        if not self.is_checked(code):
            return False

        if level < levels_count - 1:
            if level == 1:
                self.player.brumbrum(screen)
                self.player.change_level(screen, 'WHERE ARE YOU?')
            elif level == 2:
                self.player.change_level(screen, '! ! ! ! !  RUN  ! ! ! ! !')
            else:
                self.player.change_level(screen, 'WHERE ARE YOU?')
            self.player.game.num_level += 1
            self.player.game.new_game()

        return True
